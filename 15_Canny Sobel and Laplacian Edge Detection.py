# ## Detection Edges of an Image

#Import necessary libraries
import cv2
import numpy as np

#Load Input Image
imagedata_original = cv2.imread('bugatti.jpg', 0)

#height, width = imagedata_original.shape

# Extract Sobel Edges
sobel_edg_x = cv2.Sobel(imagedata_original, cv2.CV_64F, 0, 1, ksize=5)
sobel_edg_y = cv2.Sobel(imagedata_original, cv2.CV_64F, 1, 0, ksize=5)

#Display Images
cv2.imshow('Original', imagedata_original)
cv2.waitKey(0)
cv2.imshow('Sobel X', sobel_edg_x)
cv2.waitKey(0)
cv2.imshow('Sobel Y', sobel_edg_y)
cv2.waitKey(0)

#Apply OR Operation
OR_operation = cv2.bitwise_or(sobel_edg_x, sobel_edg_y)
cv2.imshow('OR Operation', OR_operation)
cv2.waitKey(0)

#Laplacian Edge Detection
laplacian_edg_det = cv2.Laplacian(imagedata_original, cv2.CV_64F)
cv2.imshow('Laplacian Edge Detection', laplacian_edg_det)
cv2.waitKey(0)

# Canny Edge Detection
canny_edg = cv2.Canny(imagedata_original, 30, 180)
cv2.imshow('Canny Edge Detection', canny_edg)
cv2.waitKey(0)

cv2.destroyAllWindows()