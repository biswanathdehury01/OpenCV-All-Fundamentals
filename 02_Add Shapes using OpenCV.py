####################### CHAP -2 - Add Shapes

#Import necessary libraries
import cv2
import numpy as np

# Create a black image
black_image = np.zeros((1024,1024,3), np.uint8) # unit8 (Unsigned Int) is the datatype of the image 

cv2.imshow("Black Rectangle (Color)", black_image)

cv2.waitKey(0)
cv2.destroyAllWindows()


# ### Drawing a line on a black image
#
# cv2.line(image, starting point/cordinates, ending point/cordinates, color, thickness)

# Draw a flourescent green diagonal line of thickness of 4 pixels

#Image
black_image = np.zeros((512,512,3), np.uint8)

#Draw Line
cv2.line(black_image, (1,1), (250,250), (100,255,0), 4)
cv2.imshow("Flourescent Line", black_image)

cv2.waitKey(0)
cv2.destroyAllWindows()



#########################

# ### Drawing a circle on a black image
#
# cv2.cirlce(image, center, radius, color, fill)

# Draw a blue circle of thickness of 4 pixels

#Image
black_image = np.zeros((512,512,3), np.uint8)

#Draw Circle
cv2.circle(black_image, (200, 200), 75, (255,0,0), 4)
cv2.imshow("Circle", black_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#########################
    
# ### Drawing a rectangle on a black image
#
# cv2.rectangle(image, starting vertex, opposite vertex, color, thickness)
# Draw a Grey rectangle

#Image
black_image = np.zeros((512,512,3), np.uint8)

#Draw REctangle
cv2.rectangle(black_image, (50,100), (250,250), (110,110,90), -1)
cv2.imshow("Rectangle", black_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ### Add Text
#
# cv2.putText(image, 'Text to Display', bottom left starting point, Font, Font Size, Color, Thickness)
#
# - FONT_HERSHEY_SCRIPT_SIMPLEX
# - FONT_HERSHEY_SCRIPT_COMPLEX
# - FONT_HERSHEY_DUPLEX,FONT_HERSHEY_COMPLEX
# - FONT_HERSHEY_TRIPLEX, FONT_HERSHEY_COMPLEX_SMALL
# - FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN


#Add a Text to an image

#Image
black_image = np.zeros((512,512,3), np.uint8)

#Add Text
cv2.putText(black_image, 'This is Awesome!', (10,100), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (100,170,0), 3)
cv2.imshow("This is Awesome!", black_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ### Drawing a polygon on a black image


#Add a Polygon to an image

#Image
black_image = np.zeros((512,512,3), np.uint8)

# Define four points
pts = np.array( [[25,65], [415,65], [80,150], [400,500]], np.int32) # Coordinate array stored in integer format

# Reshape points in form that is required by polylines
pts = pts.reshape((-1,1,2))

#Create Polygon
cv2.polylines(black_image, [pts], True, (255,255,255), 3)
cv2.imshow("Polygon", black_image)
cv2.waitKey(0)
cv2.destroyAllWindows()