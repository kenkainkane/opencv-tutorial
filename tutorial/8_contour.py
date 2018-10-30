import cv2
import numpy as np

img = cv2.imread('../images/apple.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

lower = np.array([0, 0, 0])
upper = np.array([200, 255, 255])
mask = cv2.inRange(img, lower, upper)

# หา contours บน mask
_, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# วาด contours ลำดับที่ -1 (หมายถึงทั้งหมด) ลงบน img 
cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow('contours',img)
cv2.imshow('mask',mask)
cv2.waitKey()
cv2.destroyAllWindows()