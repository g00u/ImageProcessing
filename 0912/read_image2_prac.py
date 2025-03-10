import sys
import cv2 as cv
sys.path.append(r'C:/IMAGEPROCESSING/Common')  # 경로 추가
from utils import print_matInfo  # Common 폴더가 경로에 추가됐으므로 utils에서 직접 import

title1, title2 = 'color2gray', 'color2color'
color2gray = cv.imread("C:/temp/read_gray.jpg", cv.IMREAD_GRAYSCALE)
color2color = cv.imread("C:/temp/read_color.jpg", cv.IMREAD_COLOR)

if color2gray is None or color2color is None:
    raise Exception('영상파일 읽기 에러')

print("행렬 좌표(100,100)화소값")
print("%s %s" %(title1, color2gray[100,100]))
print("%s %s\n" %(title2, color2color[100,100]))

print_matInfo(title1, color2gray)
print_matInfo(title2, color2color)

cv.imshow(title1, color2gray)
cv.imshow(title2, color2color)
cv.waitKey(0)
cv.destroyAllWindows()
