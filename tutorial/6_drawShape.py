import cv2
import numpy as np

# สร้าง matrix 0 ขนาด 512 x 512 เก็บไว้ในตัวแปร img
img = np.zeros((512, 512, 3), np.uint8)

# วาดเส้นตรงในตัวแปร img ที่ตำแหน่ง (0, 0) ถึง (511, 511) ด้วยสีน้ำเงิน ความหนา 5 px
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# วาดวงกลมในตัวแปร img จุดศูนย์กลางที่ (200, 50) รัศมี 50px ด้วยสีแดง
# ความหนา -1 หมายถึง ระบายทึบ
cv2.circle(img, (200, 50), 50, (0, 0, 255), -1)

# กำหนดจุดเพื่อวาดรูปหลายเหลี่ยม
pts = np.array([[100,50],[200,50],[200,120],[150,10]], np.int32)
# วาดรูปหลายเหลี่ยมในตัวแปร img ตามจุดที่กำหนด รูปปิด(True) ด้วยสีเหลือง ความขนา 3 px
cv2.polylines(img, [pts], True, (0,255,255), 3)

# กำหนด font ในการเขียนข้อความลงบนภาพ
font = cv2.FONT_HERSHEY_SIMPLEX
# เขียน Hello World ลงบน img ที่ตำแหน่ง (50, 256) ด้วย font ที่กำหนด ขนาด 2 สีขาว
cv2.putText(img, 'Hello World', (50, 256), font, 2.0, (255, 255, 255), lineType=cv2.LINE_AA) 

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()