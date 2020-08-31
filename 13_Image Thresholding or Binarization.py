# ## Image Thresholding or Binarization

# Threshold has 4 arguments - Image, threshold value, maximum value, binary type
# this notebook has all the diferrent binary types

import cv2
import numpy as np

# Load our image as greyscale
imagedata_original = cv2.imread('b.jpg',0)
cv2.imshow('Original', imagedata_original)

# Values below 127 set to 0 (black), rest everything above set to 255 (white)
ret,threshold_1 = cv2.threshold(imagedata_original, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshold Binary', threshold_1)
cv2.waitKey(0)

# Values below 127 set to 255 (white), rest everything above set to 0 (black). Opposite of above
ret,threshold_2 = cv2.threshold(imagedata_original, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Threshold Binary Inverse', threshold_2)
cv2.waitKey(0)

# Values above 127 are truncated i.e shades with range 128 to 255 are set as 127.
ret,threshold_3 = cv2.threshold(imagedata_original, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow('Threshold Trunc', threshold_3)
cv2.waitKey(0)

# Values below 127 set to 0, values above 127 remain unchanged
ret,threshold_4 = cv2.threshold(imagedata_original, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow('Threshold To Zero', threshold_4)
cv2.waitKey(0)

# Values below 127 remain unchanged, values above 127 goes to 0
ret,threshold_5 = cv2.threshold(imagedata_original, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow('Threshold To Zero Inv', threshold_5)
cv2.waitKey(0)

cv2.destroyAllWindows()

# ## Adaptive Thresholding

#Import necessary libraires
import cv2
import numpy as np

# Load the input image
input_image3 = cv2.imread('input_scanned_image.jpg', 0)

cv2.imshow('Original Image', input_image3)
cv2.waitKey(0)

# Values below 127 set to 0 (black), rest everything above set to 255 (white)
ret,threshold_1 = cv2.threshold(input_image3, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshold Binary', threshold_1)
cv2.waitKey(0)

# Blur the image
blurred_image = cv2.GaussianBlur(input_image3, (3, 3), 0)

# Using adaptiveThreshold
adp_thresholding = cv2.adaptiveThreshold(blurred_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
cv2.THRESH_BINARY, 3, 5)
cv2.imshow('Adaptive Thresholdin', adp_thresholding)
cv2.waitKey(0)

cv2.destroyAllWindows()
