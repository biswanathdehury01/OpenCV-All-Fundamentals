# ## Rotation and Flip using OpenCV
#
# cv2.getRotationMatrix2D(rotation_center_x, rotation_center_y, angle of rotation, scale)

# In[1]:

#Import necessary libraries
import cv2
import numpy as np

#Load/Read input image
input_image = cv2.imread('b.jpg')
cv2.imshow('Original Image', input_image)

#Extract height and width of the image
height, width = input_image.shape[:2]

# Divide by four to rotate the image around its centre
# cv2.getRotationMatrix2D(rotation_center_x, rotation_center_y, angle of rotation, scale)
rotation_mat_R = cv2.getRotationMatrix2D((width/2, height/2), 45, .5)

# 
rotated_image_output = cv2.warpAffine(input_image, rotation_mat_R, (width, height))

cv2.imshow('Rotated Image', rotated_image_output)
cv2.waitKey()
cv2.destroyAllWindows()

# ### Flipping Images

# In[3]:

# Flipping image horizontally, by using flip function
flipped_img_hor = cv2.flip(input_image, 1) # you can filp horizontally =1, Vertically 0
cv2.imshow('Horizontal Flip', flipped_img_hor)

flipped_img_Ver = cv2.flip(input_image, 0) # you can filp horizontally =1, Vertically 0
cv2.imshow('Vertical Flip', flipped_img_Ver)
cv2.waitKey()
cv2.destroyAllWindows()