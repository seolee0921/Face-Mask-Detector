import cv2
import face_recognition
from PIL import Image, ImageDraw

face_cascade = cv2.CascadeClassifier('xml\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('xml\haarcascade_eye_tree_eyeglasses.xml')
video_path = 'data\example3.mp4'
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y , w ,h) in faces:
        print("face =", x, y, w, h)
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey ,ew, eh) in eyes:
            print("eye =",ex, ey, ew, eh)
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 5)

    # Display the output
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()