import numpy as np
import cv2 as cv

blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)
image = np.zeros((400, 600, 3), np.uint8)
print(image)
image[:] = (255, 255, 255)
print(image)

pt1, pt2 = (50, 50), (250, 150)
pt3, pt4 = (400, 150), (500, 50)
roi = (50, 200, 200, 100)

## 직선 그리기
cv.line(image, pt1, pt2, red)
cv.line(image, pt3, pt4, green, 3, cv.LINE_AA) # 계단 현상 감소선

## 사각형 그리기
cv.rectangle(image, pt1, pt2, blue, 3, cv.LINE_4)
cv.rectangle(image, roi, red, 3, cv.LINE_8)
cv.rectangle(image, (400, 200, 100, 100), green, cv.FILLED)

cv.imshow("Line & Rectangle", image)
cv.waitKey(0)
cv.destroyAllWindows()