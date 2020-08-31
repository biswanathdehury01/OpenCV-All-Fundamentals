# ## Cropping_an_Image
#
#

import cv2
import numpy as np

imagedata_crop = cv2.imread('b.jpg')
height, width = imagedata_crop.shape[:2]

# Extract the pixel coordiantes (starting from top left)
start_row, start_col = int(height * .20), int(width * .20)

# Extract the pixel coordiantes (ending to bottom right)
end_row, end_col = int(height * .80), int(width * .80)

# Using indexing method to crop the desired rectangle area
cropped_image = imagedata_crop[start_row:end_row , start_col:end_col]

#Display Original and Cropped Images
cv2.imshow("Original Image", imagedata_crop)
cv2.waitKey(0)
cv2.imshow("Cropped Image", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()