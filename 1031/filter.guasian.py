import numpy as np, cv2

image = cv2.imread("images\smoothing.jpg",cv2.IMREAD_GRAYSCALE)
ksize = (5,17) # 가로(표준편차가 작고) x 세로(표준편차가 큼)로 표현이 됨
gaussian_1dX = cv2.getGaussianKernel(ksize[0],0, cv2.CV_32F)
gaussian_1dY = cv2.getGaussianKernel(ksize[1],0,cv2.CV_32F)

gauss_img1 = cv2.GaussianBlur(image, ksize, 0)
gauss_img2= cv2.sepFilter2D(image, -1, gaussian_1dX, gaussian_1dY)

titles = ['image', 'gauss_img1', 'gauss_img2']
[cv2. imshow(t, eval(t)) for t in titles]
cv2.waitKey(0)