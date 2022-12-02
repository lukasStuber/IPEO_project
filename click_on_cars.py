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
right_clicks = list()
idx_x = 0
idx_y = 0
size_x = 500
size_y = 300
is_done = False

# get the path of the image
file_path = os.path.realpath(__file__)
path_image = os.path.dirname(file_path) + '\\Data_images\swissimage-dop10_2022_2690-1253_0.1_2056.tif'

# import the image
img = cv2.imread(path_image,1)
np_img_full = np.array(img, dtype=np.uint8)[0:1800, 0:3000]
np_img = np_img_full[0:size_y, 0:size_x]
full_size_y, full_size_x, _ = np_img_full.shape

# number of segments for the slic algorithm
nb_segments = 300

# create the window
window = "image"
cv2.namedWindow(window)
cv2.resizeWindow(window, size_x, size_y)


#this function will be called whenever the mouse is right-clicked
def capture_event(event, x, y, flags, params):
    #right-click event value is 2
    if event == cv2.EVENT_RBUTTONDOWN :
        global right_clicks, segments, np_img, idx_x, idx_y

        #store the coordinates of the right-click event
        right_clicks.append([idx_x*size_x+x, idx_y*size_y+y])
        idx = (segments == segments[y,x])
        np_img[idx] = [0, 0, 255]

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
    segments = slic(np_img, n_segments=nb_segments)
    cv2.imshow(window, np_img)
    k = cv2.waitKey(1)
    if k == 13:         # enter
        next_image()
        if is_done: break
    if k == 27: break   # esc
    if is_done: break

cv2.destroyAllWindows()
print("\n The right clicks are: \n", right_clicks, '\n')