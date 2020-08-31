# ## Blob Detection

# Import necessary libraries
import cv2
import numpy as np;

# Load Input Image
imagedata_original = cv2.imread("BOLB_Sunflower.jpg", 0)
cv2.imshow("Input Image", imagedata_original)
cv2.waitKey(0)

# Set up the detector with default parameters.
detectorobj = cv2.SimpleBlobDetector_create()

# Detect blobs
keypoint_info = detectorobj.detect(imagedata_original)

# Highlight detected blobs as blue circles.
blank_img = np.zeros((2,2))
blobs = cv2.drawKeypoints(imagedata_original, keypoint_info, np.array([]), (255,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# you can explore with various CV2 Draw_Matches

# Display Blobs in the image
cv2.imshow("Displaying Blobs", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()