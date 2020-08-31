# ## Line Detection
#

# Import necessary libraries
import cv2
import numpy as np

#Load input image
imagedata_original = cv2.imread('Lines.jpg')

# Perform Grayscaling and Canny Edge Detection
grayscale_img = cv2.cvtColor(imagedata_original, cv2.COLOR_BGR2GRAY)
canny_edges = cv2.Canny(grayscale_img, 100, 170, apertureSize = 3)

# Display Canny Edges
cv2.imshow("Canny Edges", canny_edges)
cv2.waitKey(0)

# Houghlines function to detect lines
line_info = cv2.HoughLines(canny_edges, 1, np.pi/180, 200)

# Iterate through each line and convert it to cv.lines required format i.e. get desired end points
for line in line_info:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(imagedata_original, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Display the image
cv2.imshow('Hough Lines Generated', imagedata_original)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ## Probabilistic Hough Line Detection
#
# cv2.HoughLinesP(input image, 𝜌 accuracy, 𝜃 accuracy, threshold, minimum line length, max line gap)
#


#Import necessary libraries
import cv2
import numpy as np

# Load Input Image
imagedata_original = cv2.imread('Lines.jpg')

# Perform Grayscaling and Canny Edge Detection
grayscale_img = cv2.cvtColor(imagedata_original, cv2.COLOR_BGR2GRAY)
canny_edges = cv2.Canny(grayscale_img, 100, 170, apertureSize = 3)

#Display Canny edges
cv2.imshow("Canny Edges", canny_edges)
cv2.waitKey(0)

# Probabilistic Houghlines function to detect lines
line_info = cv2.HoughLinesP(canny_edges, 1, np.pi / 180, 250, 110, 10)

# Get desired end points
for line in line_info:
    for x1,y1,x2,y2 in line:
        cv2.line(imagedata_original, (x1, y1), (x2, y2),(255, 0, 0), 2)

# Display the image
cv2.imshow('Probabilistic Hough Lines Generated', imagedata_original)
cv2.waitKey(0)
cv2.destroyAllWindows()