# ### Drawing a Shape by dragging with Mouse button

#Import necessary libraries
import cv2
import numpy as np

# Define mouse pressed and mouse position paramters
draw = False # Will be changed to when mouse is pressed
ix,iy = -1,-1 # Mouse position

# Create a rectangle shape function to draw a blue rectangle when mouse is dragged
def rectangle_shape(event,x,y,flagval,par):
    global draw,ix,iy

    if event == cv2.EVENT_LBUTTONDOWN:
        # Value of variable draw will be set to True, when you press DOWN left mouse button
        draw = True
        # mouse location is captured here
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        # Dragging the mouse at this juncture
        if draw == True:
        # If draw is True then it means you've clicked on the left mouse button
        # Here we will draw a rectangle from the previous position to the x,y where the mouse is currently located
            cv2.rectangle(image_window,(ix,iy),(x,y),(255,0,0),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        # As soon as you release the the mouse button, variable draw will be set as False
        draw = False
        # Here we are completing to draw the rectangle on image window
        cv2.rectangle(image_window,(ix,iy),(x,y),(255,0,0),-1)

# Creating a black image window
image_window = np.zeros((1024,1024,3), np.uint8)

# Naming the window for reference
cv2.namedWindow(winname='Image_Window')

# # Connecting the mouse button to the callback function
cv2.setMouseCallback('Image_Window',rectangle_shape)

while True: #Keep the black image window open until we break with Esc key on keyboard

    # Showing the image window
    cv2.imshow('Image_Window',image_window)
    
    # Coming out of window by pressing Escape key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()