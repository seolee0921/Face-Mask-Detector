import face_recognition
from PIL import Image, ImageDraw

image_path = 'data/without_mask/augmented_image_20.jpg'

face_image_np = face_recognition.load_image_file(image_path)
face_locations = face_recognition.face_locations(face_image_np)

face_image = Image.fromarray(face_image_np)
draw = ImageDraw.Draw(face_image)

for face_location in face_locations:
    top = face_location[0]
    right = face_location[1]
    bottom = face_location[2]
    left = face_location[3]
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 255, 255), width=4)

face_image.show()