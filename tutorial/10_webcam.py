import numpy as np
import cv2

# รับภาพจาก device 0 (1, 2, 3, ...)
cap = cv2.VideoCapture(0)

while(True):

    # ret คือการรับภาพจาก device เป็น True ถ้ามีภาพ
    # frame คือภาพจาก device
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#หยุดรับภาพ
cap.release()
cv2.destroyAllWindows()
