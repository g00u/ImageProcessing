import numpy as np, cv2
image = cv2.imread("C:/IMAGEPROCESSING/images/dft_240.jpg", cv2.IMREAD_GRAYSCALE)

def calc_spectrum(complex):
    dst = cv2.magnitude(complex[:,:,0],complex[:,:,1])
    dst = cv2.log(dst+1)
    cv2.normalize(dst, dst, 0, 255, cv2.NORM_MINMAX)
    return cv2.convertScaleAbs(dst)

dft3 = cv2.dft(np.float32(image),flags=cv2.DFT_COMPLEX_OUTPUT)

spectrum3 = calc_spectrum(np.fft.fftshift(dft3))
idft3 = cv2.idft(dft3, flags=cv2.DFT_SCALE)[:,:,0]

cv2.imshow('image',image)
#cv2.imshow('dft3', dft3)
cv2.imshow('spectrum3', spectrum3)
#cv2.imshow('idft3', idft3)
cv2.waitKey(0)