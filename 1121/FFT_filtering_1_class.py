import numpy as np, cv2


def calc_spectrum(complex):
    dst = cv2.magnitude(complex[:,:,0],complex[:,:,1])
    dst = cv2.log(dst+1)
    cv2.normalize(dst, dst, 0, 255, cv2.NORM_MINMAX)
    return cv2.convertScaleAbs(dst)

image = cv2.imread('C:/IMAGEPROCESSING/images/filter.jpg',cv2.IMREAD_GRAYSCALE)
cy,cx = np.divmod(image.shape, 2)[0]
mode = 3

dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
spectrum = calc_spectrum(np.fft.fftshift(dft))

lowpass = np.zeros(dft.shape, np.float32)
highpass = np.ones(dft.shape, np.float32) 
cv2.circle(lowpass, (cx, cy), 30, (1,1), -1)
cv2.circle(highpass,(cx,cy), 30,(0,0),-1)

lowpassed_dft = np.fft.fftshift(dft) * lowpass
highpassed_dft = np.fft.fftshift(dft) * highpass
lowpassed_img = cv2.convertScaleAbs(cv2.idft(np.fft.fftshift(lowpassed_dft),
                                             flags=cv2.DFT_SCALE|cv2.DFT_REAL_OUTPUT)) #dft 실수부 허수부 다 포함 ==>스케일 맞추고, 실수>허수로 바뀌는 부분 적절히 처리해서 실수값으로 반환하라
highpassed_img = cv2.convertScaleAbs(cv2.idft(np.fft.fftshift(highpassed_dft),
                                             flags=cv2.DFT_SCALE|cv2.DFT_REAL_OUTPUT))

cv2.imshow('image', image)
cv2.imshow('lowpassed_img',lowpassed_img)
cv2.imshow('highpassed_img',highpassed_img)
cv2.imshow('spectrum', spectrum)
cv2.imshow('lowpassed_spect', calc_spectrum(lowpassed_dft))
cv2.imshow('highpassed_spect', calc_spectrum(highpassed_dft))

cv2.waitKey(0)
