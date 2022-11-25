import urllib
import cv2
from win32api import GetSystemMetrics
from skimage.segmentation import slic
import numpy as np

#the [x, y] for each right-click event will be stored here
right_clicks = list()

#this function will be called whenever the mouse is right-clicked
def mouse_callback(event, x, y, flags, params):
    #right-click event value is 2
    if event == cv2.EVENT_RBUTTONDOWN :
        global right_clicks, segments, np_img_copy

        #store the coordinates of the right-click event
        right_clicks.append([x, y])
        idx = (segments == segments[y,x])
        np_img_copy[idx] = 0
        
        cv2.destroyAllWindows()
        #print(right_clicks)

path_image = "C:\\Users\lukas\Documents\_EPFL\Image Processing\Project\swissimage_cropped2.tif"
img = cv2.imread(path_image,0)
np_img = np.array(img, dtype=np.uint8)
np_img_copy = np.copy(np_img)
print(np_img.shape)

scale_width = 640 / img.shape[1]
scale_height = 480 / img.shape[0]
scale = min(scale_width, scale_height)
window_width = int(img.shape[1] * scale)
window_height = int(img.shape[0] * scale)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', window_width, window_height)

segments = slic(np_img, n_segments=1000, sigma=1)
print(segments.shape)

#set mouse callback function for window
cv2.setMouseCallback('image', mouse_callback)

while True:
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', window_width, window_height)
    cv2.imshow('image', np_img_copy)
    if cv2.waitKey(0)==27:
        break
    cv2.destroyAllWindows()
