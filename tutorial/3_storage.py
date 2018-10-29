import cv2
import numpy as np

img = cv2.imread('../images/apple.jpg')
gray = cv2.imread('../images/apple.jpg',0)

# image.shape ใช้ตรวจสอบ row, column, channel ของภาพที่เก็บไว้ในตัวแปร
# จะเห็นได้ว่า ภาพสีจะถูกระบุไว้ทั้ง row, column และ channel
# ส่วนภาพ Grayscale จะถูกระบุแค่ row และ column
print('img ', img.shape)
print('gray ', gray.shape)

# เราสามารถทราบได้ว่าที่ row, column ที่ต้องการตรวจสอบมีค่าสีเท่าไหร่
print('img color ', img[220, 220])
print('gray color ', gray[220, 220])

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()