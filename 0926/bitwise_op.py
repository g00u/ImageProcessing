import numpy as np
import cv2

# 이미지 생성
image1 = np.zeros((300, 300), np.uint8)  # 300x300 크기의 검정색 이미지
image2 = image1.copy()  # image1을 복사하여 image2 생성

# 이미지 크기 정보
h, w = image1.shape[:2]  # 이미지의 높이와 너비
cx, cy = w / 2, h / 2  # 중심 좌표 계산

# 이미지1에 원 그리기
cv2.circle(image1, (int(cx), int(cy)), 100, 255, -1)  # 중심에 100 크기의 원 추가

# 이미지2에 사각형 그리기
cv2.rectangle(image2, (0, 0), (int(cx), h), 255, -1)  # 왼쪽 반쪽에 사각형 추가

# 비트 연산
image3 = cv2.bitwise_or(image1, image2)       # OR 연산
image4 = cv2.bitwise_and(image1, image2)      # AND 연산
image5 = cv2.bitwise_xor(image1, image2)      # XOR 연산
image6 = cv2.bitwise_not(image1)              # NOT 연산

# 이미지 표시
cv2.imshow("image1", image1)
cv2.imshow("image2", image2)
cv2.imshow("bitwise_or", image3) 
cv2.imshow("bitwise_and", image4)
cv2.imshow("bitwise_xor", image5) 
cv2.imshow("bitwise_not", image6)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 모든 창 닫기
