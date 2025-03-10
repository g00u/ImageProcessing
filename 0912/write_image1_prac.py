import cv2 as cv

image = cv.imread('C:/IMAGEPROCESSING/0912/read_color.jpg', cv.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽게 에러")

params_jpg = (cv.IMWRITE_JPEG_QUALITY,10)
params_png = (cv.IMWRITE_PNG_COMPRESSION,9)



cv.imwrite('C:/IMAGEPROCESSING/0912/write_test1.jpg',image)
cv.imwrite('C:/IMAGEPROCESSING/0912/write_test2.jpg',image, params_jpg)
cv.imwrite('C:/IMAGEPROCESSING/0912/write_test3.png',image,params_png)
cv.imwrite('C:/IMAGEPROCESSING/0912/write.test4.bmp',image)
print("저장완로")