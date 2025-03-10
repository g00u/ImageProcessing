import numpy as np
import cv2 as cv

image = np.zeros((200,400), np.uint8) #np.zero:영행렬
image[:]=100
image[1:10, :]=255

title1, title2 = 'Position1','position2'
cv.namedWindow(title1, cv.WINDOW_AUTOSIZE)
cv.namedWindow(title2)
cv.moveWindow(title1,150,150)
cv.moveWindow(title2,400,50)

cv.imshow(title1, image)
cv.imshow(title2, image)
cv.waitKey(0)
cv.destroyAllWindows()