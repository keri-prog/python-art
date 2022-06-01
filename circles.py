import random
import math
import numpy as np
import cv2

size = 1000
center = size//2
radiusb = size//4
radius = size//8
num_circles = 20

img = np.zeros((size, size, 3))

for i in range(-num_circles, num_circles):
    x1, y1 = [center + int(radiusb*math.cos(i*math.pi/num_circles)),
              center + int(radiusb*math.sin(i*math.pi/num_circles))]
    cv2.circle(img, (x1, y1), radius, (255, 255, 255), 2)
cv2.imwrite(f'./images/circles{num_circles}-{radiusb}-{radius}.png', img)
