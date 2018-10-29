import cv2
import numpy as np

gray = cv2.imread('../images/apple.jpg',0)

# แปลงภาพ channel เดียว เป็นภาพ binary
# พารามิเตอร์ตัวแรกคือ ภาพgrayscale
# พารามิเตอร์ตัวที่สอง ค่า threshold ที่จะเป็นตัวแบ่ง ถ้าน้อยกว่าจะเป็น 0 มากกว่าเป็น 1
# พารามิเตอร์ตัวที่สาม ค่าสีที่จะแสดงใน pixel ที่มีค่าเกิน ค่า threshold
# พารามิเตอร์ตัวที่สี่ Type

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

'''
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)
'''

cv2.imshow('binary image', thresh)
cv2.waitKey()
cv2.destroyAllWindows()