# ## Adjust Image Brightness or Darkness

#Import Necessary Libraries
import cv2
import numpy as np

#Load Original Image
imagedata_brt = cv2.imread('b.jpg')
cv2.imshow("Original", imagedata_brt)

# Matrix of ones which is multiplied by a scaler value of 60, matrix has dimesions same as our input image
Intensity_Matrix = np.ones(imagedata_brt.shape, dtype = "uint8") * 60

#Print Intensity matrix
print(Intensity_Matrix)

# Add Intensity Matrix to input image in order to increase the brightness
brightened_image = cv2.add(imagedata_brt, Intensity_Matrix)
cv2.imshow("Bright", brightened_image)

# Subtract Intensity Matrix from input image in order to decrease the brightness
darkened_image = cv2.subtract(imagedata_brt, Intensity_Matrix)
cv2.imshow("Dark", darkened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()