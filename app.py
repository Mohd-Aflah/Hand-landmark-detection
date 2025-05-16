from flask import Flask, render_template, Response
import cv2
import mediapipe as mp
import numpy as np
import threading

app = Flask(__name__)

# MediaPipe hands setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Shared resources
frame_lock = threading.Lock()
shared_frame = None
shared_count = 0

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

def capture_and_process_frames():
    global shared_frame, shared_count, frame_lock

    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(
        max_num_hands=2,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.6
    ) as hands:
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                break

            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frame_rgb)

            finger_count = 0
            if results.multi_hand_landmarks and results.multi_handedness:
                for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    label = handedness.classification[0].label  # 'Left' or 'Right'
                    finger_count += count_fingers(hand_landmarks, label)

            # Update shared data
            with frame_lock:
                shared_frame = frame.copy()
                shared_count = finger_count

        cap.release()

def generate_video_stream():
    global shared_frame, frame_lock
    while True:
        with frame_lock:
            if shared_frame is not None:
                success, encoded_image = cv2.imencode('.jpg', shared_frame)
                if success:
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + 
                           encoded_image.tobytes() + b'\r\n')

def generate_finger_count():
    global shared_count
    while True:
        yield f"data: {shared_count}\n\n"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_video_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/count')
def count():
    return Response(generate_finger_count(), mimetype='text/event-stream')

if __name__ == '__main__':
    thread = threading.Thread(target=capture_and_process_frames)
    thread.daemon = True
    thread.start()
    app.run(debug=True, threaded=True, use_reloader=False)
