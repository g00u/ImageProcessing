import numpy as np, cv2

image = cv2.imread("images/morph.jpg",cv2.IMREAD_GRAYSCALE)
mask = np.array([[0,1,0],[1,1,1],[0,1,0]]).astype('uint8')
#이진화작업
th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]
dst1= cv2.morphologyEx(th_img, cv2.MORPH_OPEN,mask)
dst2= cv2.morphologyEx(th_img, cv2.MORPH_CLOSE,mask,iterations=1)

cv2.imshow('open', dst1)
cv2.imshow('close', dst2)
cv2.waitKey(0)