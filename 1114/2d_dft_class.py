import numpy as np, cv2

def calc_spectrum(complex):
    dst = cv2.magnitude(complex[:,:,0],complex[:,:,1])
    dst = cv2.log(dst+1)
    cv2.normalize(dst, dst, 0, 255, cv2.NORM_MINMAX)
    return cv2.convertScaleAbs(dst)

image = cv2.imread("C:/IMAGEPROCESSING/images/dft_240.jpg",cv2.IMREAD_GRAYSCALE)
image_float = np.float32(image)
dft = cv2.dft(image_float, flags=cv2.DFT_COMPLEX_OUTPUT)

spercturm1 = calc_spectrum(dft)
spercturm2 = np.fft.fftshift(spercturm1)
# re_image = cv2.idft(dft, flags=cv2.DFT_SCALE)[:,:,0]
re_image = cv2.idft(dft, flags=cv2.DFT_SCALE| cv2.DFT_REAL_OUTPUT) #역변환
cv2.normalize(re_image, re_image, 0, 255, cv2.NORM_MINMAX)
re_image = np.uint8(re_image)

cv2.imshow('image', image)
cv2.imshow('spectrum1', spercturm1)
cv2.imshow('spectrum2', spercturm2)
cv2.imshow('idft_image', re_image) 
cv2.waitKey()
