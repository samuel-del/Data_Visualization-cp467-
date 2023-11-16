from PIL import Image
from numpy import save 
import cv2

import numpy as np

# def apply(): 
    # in the first part we are doing image adding 
image1 = cv2.imread("landscape.jpg")
image2 = cv2.imread("mountain.jpg")
    
# cv2.addWeighted is applied over the
# image inputs with applied parameters
image1 = np.resize(image1, image2.shape)

adding = image1 + image2 
# the window showing output image
# with the weighted sum
cv2addition = cv2.add(image1, image2)
    # elif user == '-': 
    #     pass
    # elif user == '*':
    #     pass 
    # elif user == '/': 
    #     pass 
    # else: 
    #     pass 

