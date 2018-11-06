import cv2
import numpy as np

img = cv2.imread('../images/apple.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

lower = np.array([0, 0, 0])
upper = np.array([210, 255, 255])
mask = cv2.inRange(img, lower, upper)

# Denoise by using blur function
blur = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('img', img)
cv2.imshow('blur', blur)
cv2.waitKey()
cv2.destroyAllWindows()

# Using Morphological operation
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(mask, kernel, iterations = 1)
erosion = cv2.erode(mask, kernel, iterations = 1)
cv2.imshow('dilation', dilation)
cv2.imshow('erosion', erosion)
cv2.waitKey()
cv2.destroyAllWindows()
