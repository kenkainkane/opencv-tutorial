# import library
import cv2
import numpy as np

# เก็บภาพ 'apple.jpg' ไว้ในตัวแปร img ด้วยคำสั่ง cv2.imread()
img = cv2.imread('../images/apple.jpg')

# แสดงภาพที่เก็บไว้ในตัวแปรด้วยคำสั่ง cv2.imshow()
# พารามิเตอร์ตัวแรกเป็นชื่อ window พารามิเตอร์ตัวที่สองเป็นชื่อตัวแปร
cv2.imshow('display', img)

# รอรับ input จากคีย์บอร์ดด้วยคำสั่ง cv2.waitKey()
# หน่วยเป็น milliseconds, 0 = รอจนกว่าจะมี input
cv2.waitKey(0)

# ทำลายหน้าต่างที่เปิดทั้งหมด, ถ้าไม่มีอาจทำให้โปรแกรมค้าง
cv2.destroyAllWindows()