# # Sorting Contours in a Image

# ## Get Image Contours


# Import necessary images
import cv2
import numpy as np

# Load the input image
imagedata_original = cv2.imread('Shapes.png')
cv2.imshow('Original Input Image', imagedata_original)
cv2.waitKey(0)

# Make a copy of the original image
duplicate_img = imagedata_original

# Creating a black image with dimensions same as the loaded input image
black_img = np.zeros((imagedata_original.shape[0], imagedata_original.shape[1], 3))

# Make the Color Image as Grayscale
grayscale_img = cv2.cvtColor(imagedata_original,cv2.COLOR_BGR2GRAY)

# Detect Canny Edges
canny_edged_img = cv2.Canny(grayscale_img, 40, 250)
cv2.imshow('Canny Edges on Image', canny_edged_img)
cv2.waitKey(0)

#Finding the contours on the image
contours, hierarchy = cv2.findContours(canny_edged_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

#Drawing each and every contour
cv2.drawContours(black_img, contours, -1, (255,0,0), 3)
cv2.imshow('Showing Contours over black image', black_img)
cv2.waitKey(0)

# Draw each and every contours over black image
cv2.drawContours(imagedata_original, contours, -1, (255,0,0), 3)
cv2.imshow('Showcasing all the Contours', imagedata_original)
cv2.waitKey(0)

# Detect contours and print the count of them
print ("Number of contours detected = ", len(contours))

cv2.destroyAllWindows()


######################################################
# ## Sorting By Area ## #
######################################################

# Import necessary libraries
import cv2
import numpy as np

# Load the input image
imagedata_original = cv2.imread('Shapes.png')

#Make a copy of the original image
duplicate_img = imagedata_original

# Function to display contour area
def find_contour_areas(contours):
    areas = []
    for cnt in contours:
        cont_area = cv2.contourArea(cnt)
        areas.append(cont_area)
        return areas

# Printing the areas before sorting contours
print("Contour areas before sorting", find_contour_areas(contours))

# Sorting contours from larger area to smaller area
sorted_contours_by_area = sorted(contours, key=cv2.contourArea, reverse=True)

# Printing the area after sorting contours
print("Contor areas after sorting", find_contour_areas(sorted_contours_by_area))

# Iterating over the contours and drawing one contour at a time
for sc in sorted_contours_by_area:
    cv2.drawContours(duplicate_img, [sc], -1, (0,0,255), 3)
    cv2.waitKey(0)
    cv2.imshow('Highlight Contours by Area on pressing Enter Key', duplicate_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

##########################################################
# ## Sorting By Spatial Position ## #
##########################################################


#Import necessary libraries
import cv2
import numpy as np

# Load the input image
imagedata_original = cv2.imread('Shapes.png')

#Make a copy of the original image
duplicate_img = imagedata_original.copy()

# Function for getting x coordinate of contour
def ret_x_cord_contour(contours):
    if cv2.contourArea(contours) > 10: # checks if countour is greater than 
        cent_moment = cv2.moments(contours)
        return (int(cent_moment['m10']/cent_moment['m00']))
    else:
        pass

#Function for identifying centroid
def identify_centroid(image, centroid):
    # Places a blue circle on the centers of contours
    cent_moment = cv2.moments(centroid)
    centroid_x = int(cent_moment['m10'] / cent_moment['m00'])
    centroid_y = int(cent_moment['m01'] / cent_moment['m00'])
    
    # Draw the blue circles on the contours
    cv2.circle(imagedata_original,(centroid_x,centroid_y), 10, (255,0,0), -1)
    return image

# Sort by left to right using ret_x_cord_contour function
contours_from_left_to_right = sorted(contours, key = ret_x_cord_contour, reverse = False)

# Caculate centroids and draw them on our image
for (i, c) in enumerate(contours):
    orig = identify_centroid(imagedata_original, c)
cv2.imshow("Contour with Centroids ", imagedata_original)
cv2.waitKey(0)

# Mark the contours from left to right
for (i,c) in enumerate(contours_from_left_to_right):
    cv2.drawContours(duplicate_img, [c], -1, (0,0,255), 3)
    cent_moment = cv2.moments(c)
    centroid_x = int(cent_moment['m10'] / cent_moment['m00'])
    centroid_y = int(cent_moment['m01'] / cent_moment['m00'])
    cv2.putText(duplicate_img, str(i+1), (centroid_x, centroid_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Contours from Left to Right', duplicate_img)
    cv2.waitKey(0)
    (x, y, w, h) = cv2.boundingRect(c)

cv2.destroyAllWindows()