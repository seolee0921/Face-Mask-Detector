from PIL import Image, ImageDraw
import face_recognition
import math

image_path = 'data/without_mask/300.jpg'
mask_image_path = 'data/mask.png'

face_image_np = face_recognition.load_image_file(image_path)
face_image = Image.fromarray(face_image_np)
face_locations = face_recognition.face_locations(face_image_np)
draw = ImageDraw.Draw(face_image)

print(face_locations)

top = face_locations[0][0]
right = face_locations[0][1]
bottom = face_locations[0][2]
left = face_locations[0][3]

mask_image = Image.open(mask_image_path)
mask_image = mask_image.resize((int(right - left), int((bottom - top) / 4 * 3)))
face_image.paste(mask_image, (left, int(top / 2 + (bottom - top) / 4 * 3)), mask_image)
face_image.show()