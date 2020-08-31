# # Find Contours


#Import necessary libraries
import cv2
import numpy as np

# load the input image
imagedata_original = cv2.imread('Shapes.png')
cv2.imshow('Input Image', imagedata_original)
cv2.waitKey(0)

# Convert the image into Grayscale
grayscale_img = cv2.cvtColor(imagedata_original,cv2.COLOR_BGR2GRAY)

# Detect edges using Canny
canny_det_edges = cv2.Canny(grayscale_img, 40, 250)
cv2.imshow('Canny Detected Edges', canny_det_edges)
cv2.waitKey(0)

# Use a copy of your image e.g. edged.copy(), since findContours alters the image
edged_dup = canny_det_edges.copy()

# Identify Contours in the image
contours, hierarchy = cv2.findContours(edged_dup, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Drawing contours
cv2.drawContours(imagedata_original, contours, -1, (255,0,0), 4)

cv2.imshow('Contours', imagedata_original)
cv2.waitKey(0)
cv2.destroyAllWindows()