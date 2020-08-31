###################### CHAP 1 - Convert Color Images to Greyscale Images

#Import necessary Libraries
import cv2
import numpy as np

# Load an image using 'imread' function passing path of image as an argument
image_data = cv2.imread('mg.jpg')

# Checking the dimensions of the image which are represented as (Height, Width, Channel)
print(image_data.shape)

# Show the loaded image
cv2.imshow('First Image', image_data)
cv2.waitKey(6000) # means 6 seconds, window will get closed autometically
cv2.destroyAllWindows()

# Image can be converted to Grayscale at the loading time by passing an additional argument cv2.IMREAD_GRAYSCALE or 0
#image_data = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
image_data = cv2.imread('mg.jpg')
#image_data = cv2.imread('mg.jpg',0) # here by just giving a parameter 0 we can convert an image to grey image
#image_data = cv2.imread('mg.jpg',1) # here by just giving a parameter 1 we can convert bak to colored image
cv2.imshow('First Image', image_data)
cv2.waitKey(0) # 0 means wait for user input forever
cv2.destroyAllWindows()

#Alternative way of making an image Grayscale
image_data = cv2.imread('test.jpg')
greyscale_image = cv2.cvtColor(image_data, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image', greyscale_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Saving the image
# here we paas 2 parameters.
cv2.imwrite('out_image.jpg', image_data)

## HSV => Hue, Saturation and Value. These are nothing but ways to store images in computer.

