import cv2
import numpy as np

# Harris 코너 검출 결과 시각화 함수
def onCornerHarris(val):
    global conner2, original_image
    thresh = val  # Trackbar에서 현재 설정된 임계값 가져오기
    display = original_image.copy()  # 원본 이미지를 복사하여 시각화용으로 사용
    display[conner2 > thresh] = [0, 0, 255]  # 강도가 임계값 이상인 코너를 빨간색으로 표시
    cv2.imshow("Harris Corners", display)  # 결과 이미지 출력

# 원본 이미지 읽기
image_path = "C:/IMAGEPROCESSING/image1128/harris.jpg"
original_image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# 그레이스케일 변환
gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Harris 코너 검출
blockSize = 4  # 코너 강도를 계산할 영역 크기
apertureSize = 3  # Sobel 커널 크기
k = 0.04  # Harris 검출 민감도 매개변수
conner2 = cv2.cornerHarris(gray, blockSize, apertureSize, k)

# 코너 응답값을 8비트 형식으로 정규화
conner2 = cv2.normalize(conner2, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# Harris 코너 검출 결과 출력
cv2.imshow("Original Image", original_image)  # 원본 이미지
cv2.imshow("Harris Response", conner2)  # Harris 응답값 맵

# Trackbar 생성 (Threshold를 동적으로 조정)
cv2.namedWindow("Harris Corners")  # 결과 출력 창 생성
cv2.createTrackbar("Threshold", "Harris Corners", 125, 255, onCornerHarris)

# 초기 코너 표시
onCornerHarris(125)

# 키 입력 대기
cv2.waitKey(0)
cv2.destroyAllWindows()
