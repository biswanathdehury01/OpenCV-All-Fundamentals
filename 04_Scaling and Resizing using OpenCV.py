# ### Scaling and Resizing
#
# cv2.resize(image, dsize(output image size), x scale, y scale, interpolation)
#


# Import necessary libraries
import cv2
import numpy as np

# Read/load input image
input_image = cv2.imread('62274667.jpg')
cv2.imshow('Original Image', input_image)
cv2.waitKey()

# Making image 1/2 of it's original size
scaled_image1 = cv2.resize(input_image, None, fx=0.5, fy=0.5)
cv2.imshow('Scaled Image', scaled_image1)
cv2.waitKey()

# Making image 1.5 times the size of original image
scaled_image2 = cv2.resize(input_image, None, fx=1.5, fy=1.5, interpolation = cv2.INTER_AREA)
cv2.imshow('Scaling - Area Interpolation', scaled_image2)
cv2.waitKey()

# Skewing the resizing by setting exact dimensions
scaled_image3 = cv2.resize(input_image, (700, 250), interpolation = cv2.INTER_AREA)
cv2.imshow('Scaling - Skewed Size', scaled_image3)
cv2.waitKey()

cv2.destroyAllWindows()

# ### Image Pyramid

#Import necessary libraries
import cv2

#Load/Read an image
input_image = cv2.imread('62274667.jpg')

smaller_img = cv2.pyrDown(input_image) # this will convert to half of original size
larger_img = cv2.pyrUp(input_image) # this will conver to double of original size

cv2.imshow('Original', input_image )

cv2.imshow('Smaller ', smaller_img )
cv2.imshow('Larger ', larger_img )
cv2.waitKey(0)
cv2.destroyAllWindows()
