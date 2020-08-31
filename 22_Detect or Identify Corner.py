# ## Finding Corners

# In[1]:

# Import necessary libraries
import cv2
import numpy as np

# Load input image and covert it into grayscale
imagedata_original = cv2.imread('chess_grid.png')
cv2.imshow('Original Input Image', imagedata_original)
cv2.waitKey(0)

grayscale_img = cv2.cvtColor(imagedata_original, cv2.COLOR_BGR2GRAY)

# Change the grayscale image array to float32, the format required by cornerHarris function
grayscale_img = np.float32(grayscale_img)

# Apply cornerHarris function
harr_corner_info = cv2.cornerHarris(grayscale_img, 3, 3, 0.05)

# Apply dilation on the corner points in order to enlarge them
kernel = np.ones((7,7),np.uint8)
harr_corner_info = cv2.dilate(harr_corner_info, kernel, iterations = 2)

# Apply Threshold to change the colors of the corners we are drawing on our image.
imagedata_original[harr_corner_info > 0.025 * harr_corner_info.max() ] = [255, 127, 127]

cv2.imshow('Corner Detection using Harris Corners', imagedata_original)
cv2.waitKey(0)
cv2.destroyAllWindows()