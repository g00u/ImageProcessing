import numpy as np, cv2

block = np.zeros((8,8), np.uint8)
cv2.randn(block, 128, 50)
dct4 = cv2.dct(block.astype('float32'))
idct4 = cv2.dct(dct4, flags= cv2.DCT_INVERSE)

print("block=\n", block)
print('dct4(OpenCV 함수)=\n', dct4)
print()
print('idct4(OpenCV 함수)=\n', idct4)
