import cv2
import numpy as np

img = cv2.imread('../images/apple.jpg')

# แปลง Color Space ของภาพด้วยคำสั่ง cv2.cvtColor()
# พารามิเตอร์ตัวแรกคือ ภาพที่จะแปลง, พารามิเตอร์ตัวที่สองคือ Color Space ที่จะแปลง
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#การ Convert ภาพ BGR เป็น Grayscale
# Grat = (0.114*B + 0.587*G + 0.299*R)

# มีวิธีแปลงเป็น Grayscale อีกวิธีคือ
# gray = cv2.imread('../images/apple.jpg',0)

cv2.imshow('grayscale', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()