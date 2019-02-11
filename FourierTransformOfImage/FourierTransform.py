import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('graf[1].jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift)) ###the magnitude may thus be accordingly altered

plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Fourier Transform of the Image'), plt.xticks([]), plt.yticks([])
plt.show()