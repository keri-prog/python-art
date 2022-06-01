import random 
import numpy as np
import cv2

size = 500
num_boxes = 100

img = np.zeros((size, size, 3))

for i in range(num_boxes):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    x1, y1 = [random.randint(0, size), random.randint(0, size)]
    x2, y2 = [random.randint(0, size), random.randint(0, size)]
    cv2.rectangle(img, (x1, y1), (x2, y2), (r, g, b), 2)
cv2.imwrite(f'./images/boxes{num_boxes}.png', img)