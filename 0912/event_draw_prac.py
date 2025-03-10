import numpy as np
import cv2 as cv

def onMouse(event, x, y, flags, param):
    global title, pt

    if event == cv.EVENT_LBUTTONDOWN:
        if pt[0]<0: pt =(x,y)
        else:
            cv.rectangle(image, pt,(x,y),(255,0,0,),2)
            cv.imshow(title, image)
            pt=(-1,-1)

    elif event == cv.EVENT_RBUTTONDOWN:
        if pt[0]<0: pt =(x,y)
        
        else:
            dx,dy= pt[0]-x, pt[1]-y
            radius = int(np.sqrt(dx*dx + dy*dy))
            cv.circle(image,pt,radius,(0,0,255),2)
            cv.imshow(title, image)
            pt=(-1,-1)


image = np.full((300,500,3), (255,255,255,), np.uint8)
pt=(-1,-1)
title = "Draw Event"
cv.imshow(title, image)
cv.setMouseCallback(title, onMouse)
cv.waitKey(0)
cv.destroyAllWindows()