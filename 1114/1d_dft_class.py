import numpy as np, cv2
import matplotlib.pyplot as plt

fmax = 1000
dt = 1/fmax 
t = np.arange(0,1,dt)

g1 = np.sin(2* np.pi * 50 *t)
g2 = np.sin(2* np.pi * 120 *t)
g3 = np.sin(2* np.pi * 260 *t)

g = g1 * 0.6 + g2 * 0.9 + g3 * 0.2

#openCV dft function
g_float32 = np.float32(g).reshape(-1,1)
G_complex = cv2.dft(g_float32, flags=cv2.DFT_COMPLEX_OUTPUT) #output이 복소수가 나오게 할 것임 

G_magnitude = cv2.magnitude(G_complex[:, 0,1], G_complex[:,0,1]) #실수평면위에 표기할 것 -> 실수부, 허수부계수 > 제곱을 해서 더하면 신호의 크기를 나타냄
g_reconstructed = cv2.idft(G_complex) #오차부분이 실수가 아닌부분으로 남아있을 수 있음 >                                                        
g_reconstructed = g_reconstructed[:,0,0]/len(g)
 
N = len(g)
df = fmax/N
f = np.arange(0,N,df)

plt.figure(figsize=(10,10))
plt.subplot(3, 1, 1),plt.plot(t[0:200], g[:200]),plt.title('Original Signal')
plt.subplot(3, 1, 2),plt.plot(f, np.abs(G_magnitude)), plt.title('DFT Amplitude Spectrum')
plt.subplot(3, 1, 3),plt.plot(t[0:200], g_reconstructed[:200]), plt.title('Reconstructed Signal')
plt.show()
