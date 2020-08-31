# ### Image Translation


#Tranlation Matrix elements T = 
# | 1 0 Tx |
# | 0 1 Ty |

#Import necessary libraries
import cv2
import numpy as np

#Load/Read the input image
input_image = cv2.imread('b.jpg')
cv2.imshow('Original Image', input_image)

# Extract height and width of the image
height, width = input_image.shape[:2]
print(height, width)
print("=============")

#Translate the height and width of the image to 1/4
height_fourth, width_fourth = height/4, width/4

# Translation matrix T
# | 1 0 Tx |
# | 0 1 Ty |
T = np.float32([[1, 0, height_fourth], [0, 1, width_fourth]])

#Printing the value of Translation matrix T
print(T)

# Using warpAffine to transform the image using the translation matrix, T
translation = cv2.warpAffine(input_image, T, (width, height))

#Showing the image output
cv2.imshow('Translation', translation)
cv2.waitKey()
cv2.destroyAllWindows()



