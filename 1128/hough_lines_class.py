import numpy as np, cv2, math

# 직선을 이미지 위에 그리기 위한 함수
def draw_houghLines(src, lines, nline): #검출 직선 그리기 함수
    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR) #컬러 영상 변환
    min_length = min(len(lines),nline) #실제 검출된 직선과 요청한 직선 개수 중 최솟값 선택
    
    for i in range(min_length): #선태간 직선 개수만큼 반복
        rho, radian = lines[i, 0, 0:2] #직선의 극좌표 값(거리, 각도)
        a, b = math.cos(radian), math.sin(radian) #각도 값으로 코사인과 사인 계산
        pt = (a*rho, b*rho) #극좌표를 기준으로 점 계산
        delta = (-1000 *b, 1000*a) #직선을 확장하기 위한 이동량(큰 값 선택)
        pt1 = np.add(pt, delta).astype('int') #직선의 시작점 계산
        pt2 = np.subtract(pt, delta).astype('int') # 직선의 끝점 계산
        cv2.line(dst, tuple(pt1), tuple(pt2), (0, 255, 0), 2, cv2.LINE_AA) #계산된 두 점을 이어 직선 그리기(녹색)
    return dst

image = cv2.imread("C:/IMAGEPROCESSING/image1128/hough.jpg", cv2.IMREAD_GRAYSCALE)
blur = cv2.GaussianBlur(image, (5,5,), 2,2) 
canny = cv2.Canny(blur, 100, 200, 5)

rho, theta = 1, np.pi/180 #거리간격, 각도간격(라디안 단위)
lines2 = cv2.HoughLines(canny, rho, theta, 80) #직선 검출 임계값 80
dst2 = draw_houghLines(canny, lines2, 7) #검출된 직선을 이미지 위에 그리기 (최대 7개의 직선)

cv2.imshow("image", image)
cv2.imshow("canny", canny)
cv2.imshow("detected lines_OpenCV", dst2)
cv2.waitKey(0)

