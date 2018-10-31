import cv2
import numpy as np

img = cv2.imread('../images/apple.jpg')
result = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

lower = np.array([0, 0, 0])
upper = np.array([210, 255, 255])
mask = cv2.inRange(img, lower, upper)

# หา contours บน mask
_, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# วาด contours ลำดับที่ -1 (หมายถึงทั้งหมด) ลงบน img 
cv2.drawContours(img, contours, -1, (0,255,0), 3)
for cnt in contours :

# เราสามารถรู้ contours area
    area = cv2.contourArea(cnt)

# สร้าง condition เพื่อตัด noise
    if area > 100 :

# วาดสี่เหลี่ยมที่เล็กที่สุดที่ล้อมรอบ contours
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(result,[box],0,(0,0,255),2)

# ศูนย์กลาง, ความกว้าง/ยาว และ มุม จาก minAreaRect
        center, wh, angle = cv2.minAreaRect(cnt)
        print('Area', area)
        print('Center',center)
        print('width, height', wh)
        print('Angle', angle)

cv2.imshow('result', result)
cv2.imshow('contours',img)
cv2.imshow('mask',mask)
cv2.waitKey()
cv2.destroyAllWindows()