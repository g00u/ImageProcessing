import numpy as np, cv2

def minMax_filter(image, ksize, mode):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.uint8)
    center = ksize//2
    
    for i in range(center, rows-center):
        for j in range(center,cols-center):
            y1,y2 = i-center, i+center +1 #왼쪽 앞에, --> 우리가 원하는 필터의 크기를 씌울 수 있음
            x1,x2 = j-center, j+center +1
            mask = image[y1: y2, x1:x2]
            dst[i,j] = cv2.minMaxLoc(mask)[mode] #mode=0 --> min/  mode=1 => max
    return dst
image = cv2.imread("C:/IMAGEPROCESSING/images/min_max.jpg", cv2.IMREAD_GRAYSCALE)
minFilter_img = minMax_filter(image, 3, 0)
maxFilter_img = minMax_filter(image, 3, 1)

cv2.imshow('image', image)
cv2.imshow('min_img', minFilter_img)
cv2.imshow('max_img', maxFilter_img)

cv2.waitKey(0)