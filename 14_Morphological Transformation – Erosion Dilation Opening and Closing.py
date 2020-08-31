# ## Dilation, Erosion, Opening and Closing operations on Images


#Import necessary libraries
import cv2
import numpy as np

#Load input image
imagedata_original = cv2.imread('erosion.jpeg', 0)

cv2.imshow('Original Image', imagedata_original)
cv2.waitKey(0)

# Defining Kernel
kernel = np.ones((5,5), np.uint8)

# Erode Operation
erosion_op = cv2.erode(imagedata_original, kernel, iterations = 1)
cv2.imshow('Erosion Operation', erosion_op)
cv2.waitKey(0)

# Dilation Operation
dilation_op = cv2.dilate(imagedata_original, kernel, iterations = 1)
cv2.imshow('Dilation Operation', dilation_op)
cv2.waitKey(0)

# Opening operation for noise removal
opening_op = cv2.morphologyEx(imagedata_original, cv2.MORPH_OPEN, kernel)
cv2.imshow('Opening Operation', opening_op)
cv2.waitKey(0)

# Closing operation for noise removal
closing_op = cv2.morphologyEx(imagedata_original, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Closing Operation', closing_op)
cv2.waitKey(0)

cv2.destroyAllWindows()


