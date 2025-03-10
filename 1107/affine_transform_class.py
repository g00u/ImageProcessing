import numpy as np, cv2
image = cv2.imread("C:/IMAGEPROCESSING/images/affine.jpg",cv2.IMREAD_GRAYSCALE)

center = (200,200)
angle,scale = 30,1 #30도 회전, 크기 변경 안 함
size = image.shape[::-1] #크기는 형태의 역순

pt1 = np.array([(30, 70),(20,240),(300,110)],np.float32)
pt2 = np.array([(120, 20),(10,180),(280,260)],np.float32)

aff_mat = cv2.getAffineTransform(pt1, pt2) #3개 좌표쌍 어파인 행렬 
rot_mat = cv2.getRotationMatrix2D(center, angle, scale) #어파인 행렬

dst3 = cv2.warpAffine(image, aff_mat, size, cv2.INTER_LINEAR) #보간법 : 양성형 보간
dst4 = cv2.warpAffine(image, rot_mat, size, cv2.INTER_LINEAR)

#점 3개가 이동하는것을 나타내기 위해 ,원래의 포인트 어디로 이동했는지 나타내기 위해
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
dst3 = cv2.cvtColor(dst3, cv2.COLOR_GRAY2BGR)

for i in range(len(pt1)):
    cv2.circle(image, tuple(pt1[i].astype(int)),3,(0,0,255),2)
    cv2.circle(dst3, tuple(pt2[i].astype(int)),3,(0,0,255),2)
    
cv2.imshow('image', image)
cv2.imshow('dst3',dst3)
cv2.imshow('dst4',dst4)
cv2.waitKey(0)