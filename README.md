# 🖥️ [Live Demo Website](https://mohd-aflah.github.io/Hand-landmark-detection/)  
> Real-Time Hand Gesture Finger Counting using Flask, OpenCV & MediaPipe

---

## 🎥 Demo Video

[Watch the demo](documents/Hand&20Land%20Mark%20Detection.mp4)

---

## 📸 Screenshots

<img src="documents/Screenshot 2025-05-16 041724.png" width="600"/>
<br>
<img src="documents/Screenshot 2025-05-16 041724.png" width="600"/>
<br>
<img src="documents/Screenshot 2025-05-16 041724.png" width="600"/>

---

## 📌 Project Overview

This project is a real-time hand gesture recognition system built using **Flask**, **OpenCV**, and **MediaPipe**, designed to count the number of fingers shown in front of a webcam and display it dynamically in a web interface.

It leverages MediaPipe's landmark tracking to recognize hand landmarks, and Flask streams the annotated camera feed to a web interface using MJPEG and Server-Sent Events (SSE).

---

## 🧪 Technologies Used

- 🐍 Python 3
- 🧠 MediaPipe (Hand Landmarks)
- 🎥 OpenCV (Video Capture)
- 🌐 Flask (Web Application Framework)
- 📡 JavaScript (SSE for real-time finger count updates)

---

## 🖐️ How It Works

1. **Webcam** captures live feed using OpenCV.
2. **MediaPipe Hands** processes frames and detects hand landmarks.
3. **Finger counting logic** uses relative positions of landmarks to count raised fingers:
   - Compares thumb's x-coordinate depending on left/right hand
   - Compares each fingertip’s y-coordinate with its PIP joint
4. **Flask**:
   - Streams annotated frames via `/video_feed`
   - Sends finger count updates via `/count` using Server-Sent Events
5. **Frontend (HTML/JS)**:
   - Shows video feed
   - Displays real-time finger count next to the video

---

## 🧠 Gesture Logic Summary

| Finger | Logic Used |
|--------|------------|
| Thumb  | Tip.x compared with IP.x depending on hand label |
| Other fingers | Tip.y compared with PIP.y (if above, counted as "up") |
| Total count | All fingers "up" are counted |
| Fist | All fingers "down" triggers "clear" action (in some versions) |

---

## 🚀 How to Run This Project

1. ✅ **Install required packages**:

```bash
pip install flask opencv-python mediapipe numpy
```

2. ✅ **Make sure your folder has this structure**:

```
hand_landmark_project/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── css/
│       └── style.css
└── README.md
```

3. ✅ **Run the Flask app**:

```bash
python app.py
```

4. ✅ **Open your browser** at:

```
http://127.0.0.1:5000
```

---

## 👨‍💻 Developer Team

| Name                  | Role                        |
|-----------------------|-----------------------------|
| Mohammed Aflah        | Project Lead, Flask Backend |
| Minhaj Akavalappil    | UI/UX Frontend              |
| Mohammed Aseel        | OpenCV Integration          |
| Mohammed Jasim A.     | Testing & Documentation     |
| Najla Musthafa        | Project Guide               |

---

## 📘 About This Project

This project was developed as part of an academic submission to demonstrate the capabilities of gesture-based human–computer interaction using deep learning and real-time processing frameworks.

The report explores:
- Hand landmark theory
- Gesture classification
- Tracking vs. detection models
- UI/UX requirements and implementation

---

## 📜 License

This project is released for educational purposes only.  
You may modify, adapt, and extend the system with proper attribution to the authors.

---

🎉 Thank you for using the **Hand Gesture Finger Counter** — built to empower intuitive, touchless interaction!

