import numpy as np
import cv2 as cv

orange, blue, white = (0, 165, 255), (255, 0, 0), (255, 255, 255)
image = np.full((300, 700, 3), white, np.uint8)

pt1, pt2 = (180, 150), (550, 150)
size = (120, 60)

# cv.circle(image, pt1, 1, 0, 2)
# cv.circle(image, pt2, 1, 0, 2)

cv.ellipse(image, pt1, size, 0, 0, 360, blue, 1)
cv.ellipse(image, pt2, size, 90, 0, 180, orange, 2)

cv.imshow("타원", image)
cv.waitKey(0)
cv.destroyAllWindows()
