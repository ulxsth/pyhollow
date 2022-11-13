import numpy as np
import cv2

img = cv2.imread("debu.jpg")
rgbaImg = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)

for i in range(rgbaImg.size):
    print(rgbaImg[i])
