import numpy as np
import cv2 as cv

def onMouse(event, x, y , flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print('click mouse left')
    elif event == cv.EVENT_RBUTTONDOWN:
        print('click moust right')
    elif event == cv.EVENT_LBUTTONUP:
        print('click out left')
    elif event == cv.EVENT_RBUTTONUP:
        print('click out right')
    elif event == cv.EVENT_LBUTTONDBLCLK:
        print('더블 클릭')

image = np.full((200,200), 255, np.uint8)

title1, title2 = "Mouse Event1", "Mouse Event2"
cv.imshow(title1, image)
cv.imshow(title2, image)

cv.setMouseCallback(title1, onMouse)
cv.waitKey(0)
cv.destroyAllWindows()