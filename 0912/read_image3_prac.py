import cv2 as cv
import sys
sys.path.append(r'C:/IMAGEPROCESSING') 
from Common.utils import print_matInfo
title1, title2 = '16bit unchanged', '32bit unchanged'
color2unchanged1 = cv.imread("C:/IMAGEPROCESSING/0912/read_16.tif",cv.IMREAD_UNCHANGED)
color2unchanged2 = cv.imread("C:/IMAGEPROCESSING/0912/read_32.tif",cv.IMREAD_UNCHANGED)

if color2unchanged1 is None or color2unchanged2 is None:
    raise Exception('영상 파일 읽기 에러')

print('16/32 비트 영상 행렬 좌표(10,10)화소값')
print(title1, '원소 자료형', type(color2unchanged1[10][10][0]))
print(title1,'화소값(3원소)',color2unchanged1[10,10])
print(title2, '원소 자료형', type(color2unchanged2[10][10][0]))
print(title2,'화소값(3원소)',color2unchanged2[10,10])

cv.imshow(title1, color2unchanged1)
cv.imshow(title2, color2unchanged2)
cv.waitKey(0)
cv.destroyAllWindows()