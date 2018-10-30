import cv2
import numpy as np

# สร้าง สี่เหลี่ยม และ วงกลม
img = np.zeros((512, 512, 3), np.uint8)
square = cv2.rectangle(img.copy(), (80, 80), (431, 431), (255, 255, 255), -1)
circle = cv2.circle(img.copy(), (255, 255), 230, (255, 255, 255), -1)

# ใช้ arithmetic operation
And = cv2.bitwise_and(square, circle)
Or = cv2.bitwise_or(square, circle)
Xor = cv2.bitwise_xor(square, circle)
Not = cv2.bitwise_not(square)

cv2.imshow('square', square)
cv2.imshow('circle', circle)
cv2.imshow('And', And)
cv2.imshow('Or', Or)
cv2.imshow('Xor', Xor)
cv2.imshow('Not', Not)

cv2.waitKey()
cv2.destroyAllWindows()