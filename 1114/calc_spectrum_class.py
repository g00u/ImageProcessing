import numpy as np, cv2

def calc_spectrum(complex):
    dst = cv2.magnitude(complex[:,:,0],complex[:,:,1])
    dst = cv2.log(dst+1)
    cv2.normalize(dst, dst, 0, 255, cv2.NORM_MINMAX)
    return cv2.convertScaleAbs(dst)