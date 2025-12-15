import cv2
from fer import FER

# Initialize emotion detector
emotion_detector = FER(mtcnn=True)

# Start webcam
cap = cv2.VideoCapture(1, cv2.CAP_AVFOUNDATION)


print("Camera started. Press ESC to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect emotions
    results = emotion_detector.detect_emotions(frame)

    for result in results:
        (x, y, w, h) = result["box"]
        emotions = result["emotions"]

        # Get emotion with highest confidence
        emotion, score = max(emotions.items(), key=lambda item: item[1])

        # Draw box and label
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f"{emotion} ({score:.2f})",
                    (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (255, 255, 255),
                    2)

    cv2.imshow("Face Emotion Detection", frame)

    # ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
