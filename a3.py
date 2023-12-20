import os

from PIL import Image
import cv2

import numpy as np 

x_val = []
y_val = [] 
z_val = [] 
dir1 = 'hand_palm'
for img in os.listdir(dir1):
    path = os.path.join(dir1, img)
    # we know the image is present
    if os.path.isfile(path):
        # open the image
        image = cv2.imread(path)
        # for half the image analysis we split the image in two on the basis of width.
        [original_y, original_x, _] = image.shape
        max_x, max_y, min_x, min_y = 0, 0, original_x, original_y
        for i in range(original_x):
            for j in range(original_y):
                colour = image[j][i]
                if colour[0] <= 52 and colour[1] <= 52 and colour[2] <= 54:
                    max_x = max(max_x, i)
                    max_y = max(max_y, j)
                    min_x = min(min_x, i)
                    min_y = min(min_y, j)
        # save all the x values --> aspect ratio width/height
        x_val.append(float(abs(max_x - min_x) / abs(max_y - min_y)))
        centre = int(0.5 * (max_x - min_x))
        centre += min_x
        # left image
        counter = 0
        for i in range(min_x, centre):
            for j in range(min_y, max_y):
                colour = image[j][i]
                # pick on shades of black
                if colour[0] <= 52 and colour[1] <= 52 and colour[2] <= 54:
                    counter += 1        
        y_val.append(float(counter / (abs(max_x - min_x) * abs(max_y - min_y))))
        # right image
        counter = 0
        for i in range(centre, max_x):
            for j in range(min_y, max_y):
                colour = image[j][i]
                # pick on shades of black
                if colour[0] <= 52 and colour[1] <= 52 and colour[2] <= 54:
                    counter += 1
        z_val.append(float(counter / (abs(max_x - min_x) * abs(max_y - min_y))))

print(" x  \t y  \t z")
for i in range(len(x_val) - 1):
    print("{:0.3f}  {:0.3f}  {:0.3f}".format(x_val[i], y_val[i], z_val[i]))
