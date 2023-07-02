import cv2
import pyautogui

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Webcam', frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in eyes:
        eye_center = (x + w // 2, y + h // 2)
        pyautogui.moveTo(eye_center[0], eye_center[1])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
