# ## Understand Approximating Contours and Convex Hull

# Import necessary libraries
import numpy as np
import cv2

# Load the input image and create a copy of the original image
imagedata_original = cv2.imread('convex_hull.jpg')
imagedata_original_copy = imagedata_original.copy()
cv2.imshow('Original Image', imagedata_original_copy)
cv2.waitKey(0)

# Convert the image into greyscale format and apply thresholding
grayscale_img = cv2.cvtColor(imagedata_original, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(grayscale_img, 127, 255, cv2.THRESH_BINARY_INV)

# Finding the contours
contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# Iterate through each contour detected and then create a rectangle around it
for cont in contours:
    x,y,w,h = cv2.boundingRect(cont)
    cv2.rectangle(imagedata_original_copy,(x,y),(x+w,y+h),(0,0,255),1)
    cv2.imshow('Rectangle around object', imagedata_original_copy)

cv2.waitKey(0)

# Iterate through each contour detected and then apply contour approximation
for cont in contours:
    accuracy = 0.001 * cv2.arcLength(cont, True)
    approx = cv2.approxPolyDP(cont, accuracy, True)
    cv2.drawContours(imagedata_original_copy, [approx], 0, (127, 0, 127), 2)
    cv2.imshow('Image after applying ApproxPolyDP', imagedata_original_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()

# ## Convex Hull
#
#

# In[4]:

# Import necessary libraries.
import numpy as np
import cv2

# Load the input image and convert it into grayscale
imagedata_original = cv2.imread('convex_hull.jpg')
grayscale_img = cv2.cvtColor(imagedata_original, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original Image', imagedata_original)
cv2.waitKey(0)

# Apply thresholding on the image
ret, thresh = cv2.threshold(grayscale_img, 176, 255, 0)

# Finding the contours
contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# Sort the contors by area and then remove largest contour
n = len(contours) - 1
contours = sorted(contours, key=cv2.contourArea, reverse=False)[:n]

# Draw the convex hull by iterating through each contour
for cont in contours:
    hull = cv2.convexHull(cont)
    cv2.drawContours(imagedata_original, [hull], 0, (255, 0, 0), 2)
    cv2.imshow('Convex Hull', imagedata_original)

cv2.waitKey(0)
cv2.destroyAllWindows()