from PIL import Image, ImageDraw
import face_recognition
import cv2
import numpy as np
import math


image_path = 'data/without_mask/95.jpg'
mask_image_path = 'data/mask.png'
image = cv2.imread(image_path)
mask_image = Image.open(mask_image_path)

face_image_np = face_recognition.load_image_file(image_path)
face_image = Image.fromarray(face_image_np)
face_locations = face_recognition.face_locations(face_image_np)
draw = ImageDraw.Draw(face_image)

eye_cascade = cv2.CascadeClassifier('xml\haarcascade_eye_tree_eyeglasses.xml')
face_cascade = cv2.CascadeClassifier('xml\haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

print("1")
for (x, y, w, h) in faces:
    print("face =", x, y, w, h)
    cv2.rectangle(image, (x,y), (x+w, y+h), (255, 0 , 0), 3)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = image[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(roi_gray)

    first_position = [int(eyes[0][0]), int(eyes[0][1]) + int(eyes[0][3] / 2)]
    second_position = [int(eyes[1][0]) + int(eyes[1][2]), int(eyes[1][1]) + int(eyes[1][3] / 2)]
    print(first_position, second_position)

    tan_angle = int(abs(first_position[1] - second_position[1])) / int(abs(first_position[0] - second_position[0]))
    mask_angle = math.atan(tan_angle)
    mask_image = mask_image.resize((int(w), int(h / 4 * 3)))

    print(mask_angle)
    face_image.paste(mask_image, (x, int(y * 1.75 + (h / 10))), mask_image)

    print('eyes =', eyes)
    for (ex, ey, ew, eh) in eyes:
        print("eye =", ex, ey, ew, eh)
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

cv2.imshow('image', image)
cv2.waitKey(0)

print("2")

face_image.show()