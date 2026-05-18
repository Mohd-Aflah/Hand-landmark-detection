# 🖥️ [Live Demo Website](https://hand-landmark-detection.onrender.com/)  
> Real-Time Hand Gesture Finger Counting using MediaPipe JS, WebRTC & Flask

---


📹 Demo Video:  
[Click to Download and Watch](documents/Hand%20Land%20Mark%20Detection.mp4)

---

## 📸 Screenshots

<img src="documents/Screenshot 2025-05-16 041724.png" width="400"/>
<br>
<img src="documents/Screenshot 2025-05-16 041751.png" width="400"/>
<br>
<img src="documents/Screenshot 2025-05-16 042303.png" width="400"/>

---

## 📌 Project Overview

This project is a real-time hand gesture recognition system designed to count the number of fingers shown in front of a webcam and display it dynamically in a web interface.

It leverages **MediaPipe JS** for high-speed, zero-latency landmark tracking directly within the user's web browser. The frontend captures the camera feed securely using HTML5 WebRTC, processes it locally on the client-side for maximum privacy and performance, and **Flask** handles serving the web application.

---

## 🧪 Technologies Used

- 🌐 **MediaPipe JS** (In-Browser Hand Landmark Tracking & Drawing)
- 📡 **JavaScript / WebRTC** (Secure local camera capture)
- 🎨 **HTML5 Canvas & CSS3** (Real-time video rendering & UI)
- 🐍 **Python 3 & Flask** (Web Application Serving)
- ☁️ **Render** (Cloud Deployment)

---

## 🖐️ How It Works

1. **Webcam** captures live feed locally via the browser using HTML5 WebRTC (`navigator.mediaDevices.getUserMedia`).
2. **MediaPipe Hands JS** processes the frames entirely on the client-side, identifying 21 3D hand landmarks in real-time at 60 FPS.
3. **Finger counting logic** uses relative positions of landmarks to count raised fingers:
   - Compares thumb's x-coordinate depending on left/right hand
   - Compares each fingertip’s y-coordinate with its PIP joint
4. **HTML5 Canvas**:
   - Renders the mirrored camera feed and draws the landmark skeleton over the hand.
5. **Flask Backend**:
   - Serves the frontend assets cleanly and securely, allowing the app to be easily deployed to cloud platforms like Render without needing heavy server-side GPU processing.

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
pip install flask gunicorn
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

