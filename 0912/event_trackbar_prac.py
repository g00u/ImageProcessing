import numpy as np
import cv2 as cv
import sys
sys.stdout.reconfigure(encoding='utf-8')
def onChange(value):
    global image, title

    add_value = value - int(image[0][0])
    print("추가 화소값 add:",add_value)
    image[:]=image + add_value
    cv.imshow(title, image)
    
image = np.zeros((300,500), np.uint8)

title = 'Trackbar Event'
cv.imshow(title, image)

cv.createTrackbar('Brightness', title, image[0][0], 255, onChange)
cv.waitKey(0)
cv.destroyAllWindows()

print(image)
image[0,0]
image[0][0]