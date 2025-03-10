import numpy as np, cv2

def average_filter(image, ksize):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.uint8)
    center = ksize//2
    
    for i in range(rows):
        for j in range(cols):
            y1,y2 = i-center, i+center +1 
            x1,x2 = j-center, j+center +1
            if y1<0 or y2>rows or x1<0 or x2>cols:   #이미지가 넘어가는 경우가 발생할 수도 있기 때문에, 테두리 까만색 안나오게끔 하는 작업
                dst[i, j] = image[i,j]
            else:
                mask = image[y1: y2, x1:x2]
                dst[i,j] = cv2.mean(mask)[0]
    return dst
image = cv2.imread("C:/IMAGEPROCESSING/images/filter_avg.jpg", cv2.IMREAD_GRAYSCALE)
avg_img = average_filter(image,5)
blur_img = cv2.blur(image, (5, 5),cv2.BORDER_REFLECT)
box_img = cv2.boxFilter(image,ddepth=-1, ksize=(5,5))

cv2.imshow('image', image)
cv2.imshow('avg_img', avg_img)
cv2.imshow('blur_img', blur_img)
cv2.imshow('box_img', box_img)

cv2.waitKey(0)