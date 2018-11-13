import cv2
import numpy as np
import pyautogui
import time

upperBlue = np.array([179, 255, 255])
lowerBlue = np.array([94, 144, 201])

cap = cv2.VideoCapture(0)

def noiseRemove(bin_img):
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(bin_img, cv2.MORPH_OPEN, kernel)
    return opening

def findObj(frame):
    global result
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lowerBlue, upperBlue)
    mask = noiseRemove(mask)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(mask, 127, 255, 0)
    frame, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours :
        cv2.drawContours(frame, cnt, -1, (0, 255, 0), 1)
        rect = cv2.minAreaRect(cnt)
        center, width_height, angle = cv2.minAreaRect(cnt)
        x, y = center
        area = cv2.contourArea(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        if (area/(r*c)) > 0.005 :
            result = cv2.drawContours(result, [box], 0, (0, 0, 255), 2)
            return (x/c), (y/r)
    return -1.0,-1.0

for i in range (0,5):
    print(5-i)
    time.sleep(1)
print('START')

while True :
    ret, frame = cap.read()
    result = frame
    r, c, _ = frame.shape

    cv2.line(result,(0,int(0.3*r)),(c,int(0.3*r)),(0,0,255),3)
    cv2.line(result,(0,int(0.7*r)),(c,int(0.7*r)),(0,0,255),3)
    frame = cv2.medianBlur(frame,5)
    xRes, yRes = findObj(frame)
    if yRes > 0.7 :
        pyautogui.keyDown('down')
    if yRes < 0.3 and yRes > -1.0:
        pyautogui.keyUp('down')
        pyautogui.press('up')
    result = cv2.resize(result, None, fx=0.5, fy=0.5)
    cv2.imshow('result', result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()