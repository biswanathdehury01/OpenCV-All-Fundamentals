# ## Image Sharpening


# Import necessary libraries
import cv2
import numpy as np

# Load input image
imagedata_original = cv2.imread('b.jpg')

cv2.imshow('Original Image', imagedata_original)
cv2.waitKey(0)

# Create a shapening kernel
sharpening_filter = np.array([[-1,-1,-1],
                              [-1,9,-1],
                              [-1,-1,-1]])

# Applying kernel(s) to the input image to get the sharpened image
sharpened_image = cv2.filter2D(imagedata_original, -1, sharpening_filter)

cv2.imshow('Sharpened Image', sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()