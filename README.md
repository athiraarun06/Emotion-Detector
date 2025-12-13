# Emotion-Detector
Real-Time Face Emotion Detection (macOS / Apple Silicon Friendly)
A real-time Face Emotion Detection system that captures live webcam video, detects faces, and predicts the dominant emotion (Happy, Sad, Angry, Surprise, Neutral, etc.) using Deep Learning. Fully optimized for Apple Silicon (M1 / M2 / M3 / M4) macOS devices.

🚀 Why This Project is Unique

While face emotion detection is common, most tutorials:

Only run on images or pre-recorded videos

Ignore macOS / Apple Silicon compatibility issues

Skip real-time webcam integration

This project stands out because it:

Works seamlessly on Apple Silicon Macs using AVFoundation + TensorFlow Metal.

Provides real-time emotion detection with live webcam feed.

Uses Deep Learning + FER for accurate emotion predictions.

Handles macOS camera permission issues—something many tutorials fail to address.

🔍 Key Features

✅ Real-time face detection with OpenCV

✅ Emotion recognition via pre-trained deep learning model (FER + TensorFlow)

✅ Live overlay of emotion labels on webcam feed

✅ macOS-friendly camera handling (AVFoundation backend)

✅ Optimized for Apple Silicon (M1/M2/M3/M4)

🛠️ Tech Stack

Technology and 	Purpose

Python 3.9:	Core programming language

OpenCV:	Webcam access & image processing

TensorFlow + Keras:	Deep learning framework

FER (Facial Emotion Recognition):	Emotion prediction

NumPy:	Numerical computations

macOS AVFoundation:	Camera backend for Apple devices

📁 Project Structure
face_emotion_detection/
│
├── face_emotion_detector/
│   ├── emotion_detector.py      # Main application
│   ├── requirements.txt         # Python dependencies
│   ├── README.md                # Project documentation
│   ├── venv/                    # Virtual environment (not pushed)
└── .gitignore                   # Ignore unnecessary files

⚙️ Installation & Setup (macOS)
1️⃣ Clone the repo
git clone https://github.com/your-username/face-emotion-detection.git
cd face_emotion_detection/face_emotion_detector

2️⃣ Create & activate virtual environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ Run the Project
python emotion_detector.py


Webcam opens and detects face(s)

Live emotion label is displayed above the detected face

Press ESC to exit

🍎 macOS Camera Fix

To avoid camera permission issues on macOS:

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)


Ensures webcam opens without authorization errors

Works with macOS system privacy settings

🧠 How It Works

Capture video frames from webcam

Detect face(s) using OpenCV

Analyze face regions with deep learning model

Predict emotion (Happy, Sad, Angry, etc.)

Overlay emotion label on live video feed

📊 Supported Emotions

😄 Happy

😢 Sad

😡 Angry

😲 Surprise

😐 Neutral

😨 Fear

🤢 Disgust

🧯 Common Issues & Fixes
❌ Webcam Not Opening

Ensure camera permissions:

System Settings → Privacy & Security → Camera → Enable Terminal / Python 


Restart Terminal after granting permission

📌 Future Improvements

Multi-face emotion detection

Show emotion confidence scores

Save emotion statistics to CSV / JSON

Convert to web app with Flask / Streamlit

Train a custom emotion detection model



# This project demonstrates:

Computer Vision fundamentals

Deep Learning applications

Real-time system development

macOS hardware-level debugging

👩‍💻 Author

Athira Arun
B.Tech CSE | Interests: AI, Machine Learning, Computer Vision
