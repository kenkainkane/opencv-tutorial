import cv2
import numpy as np

def nothing(x):
    pass

lowH = 0
lowS = 0
lowV = 0
highH = 179
highS = 255
highV = 255

cv2.namedWindow('HSV Scale')

cv2.createTrackbar('lowH',  'HSV Scale', lowH , 180, nothing)
cv2.createTrackbar('highH', 'HSV Scale', highH, 180, nothing)

cv2.createTrackbar('lowS' , 'HSV Scale', lowS , 255, nothing)
cv2.createTrackbar('highS', 'HSV Scale', highS, 255, nothing)

cv2.createTrackbar('lowV' , 'HSV Scale', lowV , 255, nothing)
cv2.createTrackbar('highV', 'HSV Scale', highV, 255, nothing)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if frame is None:
        print('image is None')
        continue
#    frame = cv2.imread('img.jpg')   
    lowH = cv2.getTrackbarPos('lowH', 'HSV Scale')
    lowS = cv2.getTrackbarPos('lowS', 'HSV Scale')
    lowV = cv2.getTrackbarPos('lowV', 'HSV Scale')

    highH = cv2.getTrackbarPos('highH', 'HSV Scale')
    highS = cv2.getTrackbarPos('highS', 'HSV Scale')
    highV = cv2.getTrackbarPos('highV', 'HSV Scale')

    lower = np.array([lowH, lowS, lowV])
    upper = np.array([highH, highS, highV])

    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
    blurred = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower, upper)
    #mask = cv2.erode(mask, None, iterations=2)
    #mask = cv2.dilate(mask, None, iterations=2)

    frame = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('Original', frame)
    cv2.imshow('Frame:', mask)

    key = cv2.waitKey(200) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
