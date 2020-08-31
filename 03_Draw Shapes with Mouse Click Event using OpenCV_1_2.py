######################### Chap 3 - Draw Shapes with Mouse Click Event using OpenCV

# In[ ]:
    
# ### Drawing Blue Circles on Black Screen by Left Button Click on Mouse

# In[1]:

#Import Necessary Libraries
import cv2
import numpy as np

# Create a circle shape function to draw a circle on left button click event
def circle_shape(event,x,y,flagval,par):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image_window,(x,y),50,(255,0,0),-1)
        # (x,y) are treated as center of circle, with radius 50, with BGR, and -1 => a solid filled structure

# Naming the window so we can reference it
cv2.namedWindow(winname='Image_Window')
# Connecting the mouse button to the callback function
cv2.setMouseCallback('Image_Window',circle_shape)

# Creating a black image
image_window = np.zeros((1024,1024,3), np.uint8)

while True: #Keep the black image window open until we break with Esc key on keyboard

    # Showing the image window
    cv2.imshow('Image_Window',image_window)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()

# ### Drawing Blue Circles on Black Screen by Left Button Click & Red Color Circle on Right Button Click on Mouse

# In[2]:

#Import Necessary Libraries
import cv2
import numpy as np

# Create a circle shape function to draw a blue circle on left button click & red circle on right button click event
def circle_shape(event,x,y,flagval,par):
    if event == cv2.EVENT_LBUTTONDOWN: # left click event
        cv2.circle(image_window,(x,y),50,(255,0,0),-1)
    elif event == cv2.EVENT_RBUTTONDOWN: # Right Click Event
        cv2.circle(image_window,(x,y),50,(0,0,255),-1)


# Naming the window for reference
cv2.namedWindow(winname='Image_Window')

# Connecting the mouse button to the callback function
cv2.setMouseCallback('Image_Window',circle_shape)

# Creating a black image
image_window = np.zeros((1024,1204,3), np.uint8)

while True: #Keep the black image window open until we break with Esc key on keyboard

    # Showing the image window
    cv2.imshow('Image_Window',image_window)

    # Coming out of window by pressing Escape key
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()