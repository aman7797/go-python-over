import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../img/cute-puppy.jpg')

img2 = cv2.imread('../img/test1.jpg',cv2.IMREAD_GRAYSCALE)

new_img = cv2.resize(img2,(1000,400))

cv2.imshow("Test Image", img)
cv2.imshow("Test Image", img2)
cv2.imshow("Test Image", new_img)


plt.imshow(img)
cv2.waitKey(0)

