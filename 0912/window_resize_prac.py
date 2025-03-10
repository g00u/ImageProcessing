import numpy as np
import cv2 as cv

image = np.zeros((200, 300), np.uint8) #200 300이미지로 그린것을
image.fill(255) 

title1, title2 = 'AUTOSIZE', 'NORMAL'
cv.namedWindow(title1, cv.WINDOW_AUTOSIZE)
cv.namedWindow(title2, cv.WINDOW_NORMAL)

cv.imshow(title1, image)
cv.imshow(title2, image)
cv.resizeWindow(title1, 400, 300) #고정
cv.resizeWindow(title2, 400,300) #normal은 크기에 맞춰서 이미지 표현하는 범위에 따라 늘어남 400, 300으로 바뀌는, 하지만 행렬 값이 바뀐것은 아님


cv.waitKey(0)
cv.destroyAllWindows()