import cv2
import numpy as np


img = cv2.imread('../images/apple.jpg')

# real object ควรใช้ Color Space HSV เนื่องจากมีค่าแสงมาเกี่ยวข้อง
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# กำหนดช่วงสีของ Object
lower = np.array([0, 0, 0])
upper = np.array([200, 255, 255])

# แปลงเป็นภาพ Binary โดยช่วงที่อยู่ใน range จะเป็น 1
mask = cv2.inRange(img, lower, upper)

cv2.imshow('inrange', mask)
cv2.waitKey()
cv2.destroyAllWindows()