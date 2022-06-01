import random 
import numpy as np
import cv2

size = 50

img = np.zeros((size, size, 3))

for x in range(size):
    for y in range(size):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        img[x][y] = [r, g, b]
    
cv2.imwrite(f'./images/pixels{size}.png', img)