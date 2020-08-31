# ## Getting Perpsective Transform


#Import necessary libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

#Load/Read input image
input_image2 = cv2.imread('ba.jpg')

#show the original image
cv2.imshow('Original', input_image2)
cv2.waitKey(0)


# Cordinates of the 4 corners of the original source image
# These coordinates we get it from Paint application
orig_img_coor = np.float32([[89,1625], [2825,1649], [49,3489], [2817,3497]])

for x in range(0,4):
    cv2.circle(input_image2, (orig_img_coor[x][0], orig_img_coor[x][1]), 5, (255,0,0), -1)

#show the original image
cv2.imshow('Coordinates Marked', input_image2)
cv2.waitKey(0)

height, width = 450, 350

# Cordinates of the 4 corners of the target output
new_img_coor = np.float32([[0,0], [width,0], [0, height], [width,height]])

# Use the two sets of four points to compute the Perspective Transformation matrix, P
P = cv2.getPerspectiveTransform(orig_img_coor, new_img_coor)

perspective = cv2.warpPerspective(input_image2, P, (width, height))

cv2.imshow('warpPerspective', perspective)
cv2.waitKey(0)
cv2.destroyAllWindows()