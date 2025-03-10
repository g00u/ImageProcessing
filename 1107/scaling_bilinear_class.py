import numpy as np, cv2
image = cv2.imread("C:/IMAGEPROCESSING/images/interpolation.jpg",cv2.IMREAD_GRAYSCALE)
size = (350,400)

dst3 = cv2.resize(image,size,0,0,cv2.INTER_LINEAR) #양선형
dst4 = cv2.resize(image, size, 0, 0, cv2.INTER_NEAREST)

cv2.imshow('image', image)
cv2.imshow('bilinear', dst3)
cv2.imshow('nearest', dst4)
cv2.waitKey(0)