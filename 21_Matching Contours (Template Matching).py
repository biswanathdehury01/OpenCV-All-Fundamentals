# ## Match the Contour Shapes


# Import necessary libraries
import cv2
import numpy as np

# Loading the reference input image
input_image = cv2.imread('source_image.jpg',0)
cv2.imshow('Input Image', input_image)
cv2.waitKey()

# Loading the target image containing the shapes to be matched
target_image = cv2.imread('target_image.jpg')
target_grayscale_img = cv2.cvtColor(target_image,cv2.COLOR_BGR2GRAY)

# Apply Thresholding on both of the images
ret, thresh1 = cv2.threshold(input_image, 127, 255, 0)
ret, thresh2 = cv2.threshold(target_grayscale_img, 127, 255, 0)

# Find contours in input image
contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

# Extract the second largest contour that will treated as input image contour ecause first larget
# image depicts the boundary of entire image
sec_lar_contour = contours[1]

# Extract contours from target image
contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

# Function to iterate through each contour in the target image and compare contour shapes
for cont in contours:
    match = cv2.matchShapes(sec_lar_contour, cont, 1, 0.0)
    if match < 0.20: 
        closest_contour = cont 
    else: 
        closest_contour = [] 
        
cv2.drawContours(target_image, [closest_contour], -1, (0,0,255), 4) 
cv2.imshow('Output Image', target_image) 
cv2.waitKey() 
cv2.destroyAllWindows() 