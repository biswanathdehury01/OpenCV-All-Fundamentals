# ## Image Masking


# Import Necessary Libraries
import cv2
import numpy as np

# Draw a greyscale (Number of channel = 1) Square
square_image = np.zeros((400, 400, 1), np.uint8)
cv2.rectangle(square_image, (75, 75), (300, 300), 255, -2)
cv2.imshow("Square", square_image)
cv2.waitKey(0)

#Draw greyscale (Number of channel = 1) Circle
circle = np.zeros((400, 400, 1), np.uint8)
cv2.circle(circle, (300, 300), 75, (255,0,0), -1)
cv2.imshow("Circle", circle)
cv2.waitKey(0)

cv2.destroyAllWindows()

# ## Bitwise Operations on Shapes

# Showing the region where both square and circle intersect
AND_Operation = cv2.bitwise_and(square_image, circle)
cv2.imshow("AND Operation", AND_Operation)
cv2.waitKey(0)

# Showing the region where either square or circle is
OR_Operation = cv2.bitwise_or(square_image, circle)
cv2.imshow("OR Operation", OR_Operation)
cv2.waitKey(0)

# Showing the region where either circle or square exists
XOR_Operation = cv2.bitwise_xor(square_image, circle)
cv2.imshow("XOR Operation", XOR_Operation)
cv2.waitKey(0)

# Showing the region that isn't part of the square i.e. inverse of the square image
NOT_Operation = cv2.bitwise_not(square_image)
cv2.imshow("NOT Operation", NOT_Operation)
cv2.waitKey(0)

cv2.destroyAllWindows()

