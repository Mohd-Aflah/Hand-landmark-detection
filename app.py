import os
import base64
from flask import Flask, render_template, request, jsonify
import cv2
import mediapipe as mp
import numpy as np

app = Flask(__name__)

# MediaPipe hands setup (instantiated globally to be reused across requests)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False, 
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.6
)
mp_drawing = mp.solutions.drawing_utils

def count_fingers(hand_landmarks, hand_label):
    """
    Counts the number of fingers shown in the camera frame using landmark positions.
    Uses landmark comparisons for thumb and vertical positions for fingers.
    """
    fingers = []

    # Thumb
    if hand_label == "Right":
        fingers.append(hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x)
    else:  # Left
        fingers.append(hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x)

    # Other four fingers
    finger_tips = [8, 12, 16, 20]
    finger_pips = [6, 10, 14, 18]

    for tip, pip in zip(finger_tips, finger_pips):
        fingers.append(hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y)

    return fingers.count(True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_frame', methods=['POST'])
def process_frame():
    try:
        # Get the base64 encoded image from the client
        data = request.json['image']
        
        # Remove the 'data:image/jpeg;base64,' prefix
        encoded_data = data.split(',')[1]
        
        # Convert base64 string to numpy array and decode image
        nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Process the frame
        frame = cv2.flip(frame, 1) # Flip horizontally for selfie view
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        finger_count = 0
        if results.multi_hand_landmarks and results.multi_handedness:
            for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                label = handedness.classification[0].label  # 'Left' or 'Right'
                finger_count += count_fingers(hand_landmarks, label)

        # Encode the processed frame back to base64
        _, buffer = cv2.imencode('.jpg', frame)
        encoded_img = base64.b64encode(buffer).decode('utf-8')

        return jsonify({
            'image': 'data:image/jpeg;base64,' + encoded_img,
            'count': finger_count
        })
        
    except Exception as e:
        print("Error processing frame:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
