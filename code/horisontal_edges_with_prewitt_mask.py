import cv2
from scipy import ndimage
from skimage import img_as_ubyte, img_as_int
import numpy as np
from matplotlib import pyplot as plt

moon = cv2.imread('images/moon.jpg', 0)
img = img_as_int(moon)

prewitt_horisontal = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype = 'float64')

convolved_img = ndimage.convolve(img, prewitt_horisontal, mode = 'constant', cval = 0.0)

prewitt_horisontal_out = img_as_ubyte(convolved_img)

plt.imshow(prewitt_horisontal_out, cmap = 'gray')

plt.show()
