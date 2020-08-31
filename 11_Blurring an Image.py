# ## Image Blurring


# Import necessary libraries
import cv2
import numpy as np

# Load the input image
imagedata_original = cv2.imread('b.jpg')
cv2.imshow('Original Image', imagedata_original)
cv2.waitKey(0)

# Create a 5 X 5 kernel
kernel_size_5x5 = np.ones((5, 5), np.float32) / 25

# Convolving the kernel with an image using the fitler2D function
blurred_image = cv2.filter2D(imagedata_original, -1, kernel_size_5x5)
cv2.imshow('Kernel Size 5X5 Blurring', blurred_image)
cv2.waitKey(0)

# Create a 9 X 9 kernel
kernel_size_9x9 = np.ones((9, 9), np.float32) / 81

blurred_image2 = cv2.filter2D(imagedata_original, -1, kernel_size_9x9)
cv2.imshow('Kernel Size 9X9 Blurring', blurred_image2)
cv2.waitKey(0)

cv2.destroyAllWindows()

# ### Several other blurring methods in OpenCV


# Impor necessary libraries
import cv2
import numpy as np

# Load the input image
imagedata_original = cv2.imread('b.jpg')

# Using gaussian filter
gaussian_blur = cv2.GaussianBlur(imagedata_original, (7,7), 0)
cv2.imshow('Gaussian Blur', gaussian_blur)
cv2.waitKey(0)

# Using Normalized box filter keeping box size some odd number
avg_blur = cv2.blur(imagedata_original, (3,3))
cv2.imshow('Averaging Blur', avg_blur)
cv2.waitKey(0)

# Median Blur
median_blur = cv2.medianBlur(imagedata_original, 5)
cv2.imshow('Median Blur', median_blur)
cv2.waitKey(0)

# Using Bilateral Filter
bilateral_blur = cv2.bilateralFilter(imagedata_original, 9, 75, 75)
cv2.imshow('Bilateral Blur', bilateral_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()