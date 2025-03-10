import numpy as np, cv2

image = cv2.imread("C:/IMAGEPROCESSING/images/perspective.jpg", cv2.IMREAD_COLOR)

pts1 = np.float32([(80,40), (315,133),(75,300),(335,300)]) #변환되는 점 4개가 어디로 가는지 지정
pts2 = np.float32([(50,60), (340,60),(50,320),(340,320)])

perspect_mat = cv2.getPerspectiveTransform(pts1,pts2) #행렬을 가지고 원근감 조정이 되는
dst = cv2.warpPerspective(image, perspect_mat, image.shape[1::-1],cv2.INTER_CUBIC) 
#워프 어파인 쓰지 못하는 이유 --> 기하적인 특징이 유지/ 평행, 직선인 애들 유지/ 
#멀리있는애 땡기기도, 가까이 있는에 뒤로, 어파인 변환으로 할 수 없음 
print('[perspect_mat] = \n%s\n' %perspect_mat)

# 변환 좌표 계산 - 행렬 내적 이용 방법 ##원근 조정하기 위해 1 필요
ones = np.ones((4,1),np.float64) #1로 이루어진 어떤 것을 만들고 
pts3 = np.append(pts1, ones, axis=1) #원본 좌표 -> 동차 좌표 저장 ##1에 값을 추가하고 
pts4 = cv2.gemm(pts3, perspect_mat.T, 1, None, 1) # 좌표 변환값 계산 ##원근변환을 하기 위해서 행렬을 곱해줌

print("원본 영상 좌표 \t 목적 영상 좌표  \t\t 동차 좌표 \t\t 변환 결과 좌표")
for i in range(len(pts4)):
    pts4[i] /= pts4[i][2]

    cv2.circle(image, tuple(pts1[i].astype(int)),3,(0,255,0),-1)
    cv2.circle(dst, tuple(pts2[i].astype(int)),3,(0,255,0),-1)
cv2.imshow('image',image)
cv2.imshow('dst_perspective', dst)
cv2.waitKey(0)
