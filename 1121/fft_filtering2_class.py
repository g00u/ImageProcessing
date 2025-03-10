import numpy as np, cv2
import matplotlib.pyplot as plt

#주파수 스펙트럼을 계산하는 함수
def calc_spectrum(complex):
    #복소수 데이터에서 크기 계산
    dst = cv2.magnitude(complex[:,:,0],complex[:,:,1])
    dst = cv2.log(dst+1)#로그 스케일 변환
    cv2.normalize(dst, dst, 0, 255, cv2.NORM_MINMAX)#정규화
    return cv2.convertScaleAbs(dst)#8비트 이미지로 변환

image = cv2.imread('C:/IMAGEPROCESSING/images/filter.jpg',cv2.IMREAD_GRAYSCALE)


#DFT로 주파수 영역 변환
#실수 데이터를 복소수 형태로 변환
dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
shifted_dft = np.fft.fftshift(dft) #주파수 성분을 중앙으로 이동
# 주파수 스텍트럼 계산
spectrum = calc_spectrum(shifted_dft)

#가우시안 필터 생성
rows, cols = image.shape
center = (cols//2, rows//2)
#x, y 좌표 그리드 생성
x = np.arange(0, cols)
y = np.arange(0, rows)
x, y = np.meshgrid(x, y)
gauss_filter = np.exp(-((x - center[0])**2 + (y -center[1])**2)/(2*(30**2)))

#버터워스 필터 생성
cutoff = 30 #컷오프 주파수
order =2  #필터 차수
distance = np.sqrt((x-center[0])**2 + (y-center[1])**2)

#버터워스 필터 생성
butter_filter = 1/ (1+(distance/cutoff)**(2*order))

#필터 적용
filtered_dft1 = shifted_dft * gauss_filter[:, :, np.newaxis]
filtered_dft2 = shifted_dft * butter_filter[:, :, np.newaxis]

#역변환하여 필터링된 이미지를 복원
gauss_img = cv2.convertScaleAbs(cv2.idft(np.fft.fftshift(filtered_dft1),
                                             flags=cv2.DFT_SCALE|cv2.DFT_REAL_OUTPUT)) 

butter_img = cv2.convertScaleAbs(cv2.idft(np.fft.fftshift(filtered_dft2),
                                             flags=cv2.DFT_SCALE|cv2.DFT_REAL_OUTPUT)) 
#필터 적용 후 주파수 스펙트럼 계산
spectrum1 = calc_spectrum(filtered_dft1)
spectrum2 = calc_spectrum(filtered_dft2)

#필터 3d 시각화
plt.figure(figsize=(10,10))
ax1 = plt.subplot(332, projection='3d')
ax1.plot_surface(x,y, gauss_filter, cmap='RdPu'), plt.title("gauss_filter")
ax2 = plt.subplot(333, projection='3d')
ax2.plot_surface(x,y, butter_filter, cmap='RdPu'), plt.title("butter_filter")


titles = ['input image', 'gauss_lowpassed_image','butter_lowpasses_image',
          'imput spectrum', 'gauss_lowpassed_spectrum', 'butter_lowpassed_spectrum']
images = [image, gauss_img, butter_img, spectrum, spectrum1, spectrum2]
plt.gray()
for i, t in enumerate(titles):
    plt.subplot(3, 3, i + 4)
    plt.imshow(images[i],cmap='gray')
    plt.title(t)
plt.tight_layout()
plt.show()
