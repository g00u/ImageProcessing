import numpy as np, cv2

image = cv2.imread("C:/IMAGEPROCESSING/images/affine2.jpg",cv2.IMREAD_GRAYSCALE)

size = image.shape[::-1] #이미지 크기
center = (size[0]//2, size[1]//2) #중심좌표 계산

scale = 1.0 #크기 비율
angle = 45 #회전 각도
translation = (150,-150) #x, y 축 방향으로의 이동

#어파인 행렬
aff_mat1 = cv2.getRotationMatrix2D(center, angle, scale)
dst1 = cv2.warpAffine(image, aff_mat1, size)

#회전 없이 크기만 변경,
aff_mat2 = cv2.getRotationMatrix2D((0,0), 0, 2) #크기비율을 2
dst2 = cv2.warpAffine(image, aff_mat2, size)

#중심점에서 45도 회전, 70%축소
aff_mat3 = cv2.getRotationMatrix2D(center, 45, 0.7)
dst3 = cv2.warpAffine(image, aff_mat3, size)

#중심점에서 45도 회전, 70%축소, x축,y축으로 150평행이동(일반적 좌표평면 기준)
aff_mat4 = cv2.getRotationMatrix2D(center, 45, 0.7)
aff_mat4[0,2] += translation[0] #x축으로의 이동 값
aff_mat4[1,2] += translation[1]
dst4 = cv2.warpAffine(image, aff_mat4, size)
cv2.imshow("image", image)
cv2.imshow("dst1_only_rotate", dst1)
cv2.imshow("dst2_only_scaling", dst2)
cv2.imshow("dst3_rotate_scaling", dst3)
cv2.imshow("dst4_rotate_scaling_translate", dst4)
cv2.waitKey(0)
