import cv2
import numpy as np
image = cv2.imread("images/morph.jpg",cv2.IMREAD_GRAYSCALE)
data = [0,1,0,1,1,1,0,1,0]
mask = np.array(data,np.uint8).reshape(3,3)
#이진화작업
th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]
dst1= cv2.erode(th_img, mask)
dst2 = cv2.morphologyEx(th_img, cv2.MORPH_ERODE, mask)

cv2.imshow('image', image)
cv2.imshow('binary', th_img)
cv2.imshow('erode1', dst1)
cv2.imshow('erode2', dst2)
cv2.waitKey(0)