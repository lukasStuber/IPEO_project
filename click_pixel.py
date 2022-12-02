import urllib
import cv2
from win32api import GetSystemMetrics
from skimage.segmentation import slic
import numpy as np
import os

# np has informatics axes (down, right)
# cv2 has mathematical axes (right, down)
# so you need to invert the axes on the np stuff

#the [x, y] for each right-click event will be stored here
idx_x = 0
idx_y = 0
size_x = 500
size_y = 300
is_done = False

# number of segments for the slic algorithm
nb_segments = 300

# get the path of the image
file_path = os.path.realpath(__file__)
path_image = os.path.dirname(file_path) + '\\test_images\swissimage_cropped2.tif'

# import the image
img = cv2.imread(path_image,1)

np_img_full = np.array(img, dtype=np.uint8)[0:1800, 0:3000] #wide ass image
ORIGINAL_full=np_img_full.copy() #wide ass image that does not get modified
GROUND_TRUTH_full=np.zeros(ORIGINAL_full.shape[0:2]) #wide ass ground truth (0 if no cars, 1 if cars)

#Now for the local variables:
np_img = np_img_full[0:size_y, 0:size_x] #small image that gets modified

full_size_y, full_size_x, _ = np_img_full.shape

segments = slic(np_img_full, n_segments=nb_segments)  #IMAGE of the segments

#safe the segmentation


# create the window of small dimensions
window = "image"
cv2.namedWindow(window)
cv2.resizeWindow(window, size_x, size_y)


#this function will be called whenever the mouse is right-clicked
def capture_event(event, x, y, flags, params):
    global segments, np_img, idx_x, idx_y, GROUND_TRUTH_full, ORIGINAL_full, np_img_full
    if event == cv2.EVENT_RBUTTONDOWN :
        idx = (segments == segments[y+idx_y*size_y,x+idx_x*size_x]) #identify the indexes of the region we clicked on
        GROUND_TRUTH_full[idx]=1
        np_img_full[idx] = [148,0,211]
        #np_img=np_img_full[idx_y*size_y:(idx_y+1)*size_y, idx_x*size_x:(idx_x*1)*size_x]
    if event == cv2.EVENT_LBUTTONDOWN :
        idx = (segments == segments[y+idx_y*size_y,x+idx_x*size_x])
        GROUND_TRUTH_full[idx] = 0
        np_img_full[idx]=ORIGINAL_full[idx]
        #np_img=np_img_full[idx_y*size_y:(idx_y+1)*size_y, idx_x*size_x:(idx_x*1)*size_x]
# this function loads the next part of the image
def next_image():
    global np_img, np_img_full, idx_x, idx_y, is_done
    if (idx_x+1)*size_x >= full_size_x:
        if (idx_y+1)*size_y >= full_size_y:
            is_done = True
        else:
            idx_x = 0
            idx_y += 1
            np_img = np_img_full[idx_y*size_y:(idx_y+1)*size_y, idx_x*size_x:(idx_x+1)*size_x]

    else:
        idx_x += 1
        np_img = np_img_full[idx_y*size_y:(idx_y+1)*size_y, idx_x*size_x:(idx_x+1)*size_x]
    return


#set mouse callback function for window
cv2.setMouseCallback(window, capture_event)

while True:
    cv2.imshow(window, np_img)
    k = cv2.waitKey(1)
    if k == 13:         # enter
        next_image()
        #safe ground truth
        if is_done: break
    if k == 27: break   # esc
    if is_done: break
print(GROUND_TRUTH_full)
cv2.destroyAllWindows()