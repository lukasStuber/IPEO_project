import cv2
from skimage.segmentation import slic
from skimage.io import imsave
import numpy as np
import os


# np has algebraic axes (down, right)
# cv2 has computer image axes (right, down)
# so you need to invert the axes on the np stuff

#the [x, y] for each right-click event will be stored here
idx_x = 0
idx_y = 0

# the size of an image segment
size_x = 500
size_y = 500

is_done = False

# number of segments for the slic algorithm
nb_segments = "NUMBER_OF_SEGMENTATIONS" #300000

# get the path and name of the image
file_path = os.path.dirname(os.path.realpath(__file__))
image_name = 'YOUR_IMAGE_HERE.tif'
path_image = file_path + '/Data_images/' + image_name

# import the image
img = cv2.imread(path_image,1)

np_img_full = np.array(img, dtype=np.uint8) # full size image (10'000 x 10'000 pixels)
ORIGINAL_full = np_img_full.copy() # full size image that does not get modified
GROUND_TRUTH_full = np.zeros(ORIGINAL_full.shape[0:2], np.uint8) # full size ground truth (0 if no cars, 1 if cars)

 # first segment of 500 x 500 pixels
np_img_segment = np_img_full[0:size_y, 0:size_x]

full_size_y, full_size_x, _ = np_img_full.shape
print("the full size image is ", full_size_x, " by ", full_size_y, " pixels.")

#safe the coordinates of the clicked cars in a txt file
cars_file_name = file_path + "/Groundtruths/cars_" + image_name + ".txt"
clicks_file = open(cars_file_name, "w")
clicks_file.write("The locations of the cars in image " + image_name + "\n")
cars_list = list()

# create the window of a segment
window = "image"
cv2.namedWindow(window)
cv2.resizeWindow(window, size_x, size_y)

# apply the SLIC algorithm to get the segmentation and save the segmentation
segments = slic(np_img_full, n_segments=nb_segments)

segment_path= file_path + '/Segmentation/' + image_name + "_Segmentation.tif"
imsave(segment_path,segments)


#this function will be called whenever the mouse is right-clicked
def capture_event(event, x, y, flags, params):
    global segments, np_img_segment, idx_x, idx_y, GROUND_TRUTH_full, ORIGINAL_full, np_img_full
    # in case of a right click mark the clicked region as car
    if event == cv2.EVENT_RBUTTONDOWN :
        idx = (segments == segments[y+idx_y*size_y,x+idx_x*size_x]) #identify the indexes of the region we clicked on
        GROUND_TRUTH_full[idx] = 1
        np_img_full[idx] = [148,0,211] # color of the selected region
        cars_list.append([idx_x*size_x+x,idx_y*size_y+y])
    
    # in case of a left click mark the region as no car
    if event == cv2.EVENT_LBUTTONDOWN :
        idx = (segments == segments[y+idx_y*size_y,x+idx_x*size_x])
        GROUND_TRUTH_full[idx] = 0
        np_img_full[idx]=ORIGINAL_full[idx]
            

# this function loads the next part of the image
def next_image():
    global np_img_segment, np_img_full, idx_x, idx_y, is_done
    if (idx_x+1)*size_x >= full_size_x:
        if (idx_y+1)*size_y >= full_size_y:
            is_done = True
        else:
            idx_x = 0
            idx_y += 1
            np_img_segment = np_img_full[idx_y*size_y:(idx_y+1)*size_y, idx_x*size_x:(idx_x+1)*size_x] # move to the beginning of the next line
            # save the data from this line of segments
            cv2.imwrite(file_path+"/groundtruth.tif", GROUND_TRUTH_full)
            write_right_clicks()
    else:
        idx_x += 1
        np_img_segment = np_img_full[idx_y*size_y:(idx_y+1)*size_y, idx_x*size_x:(idx_x+1)*size_x]  # move one step to the right
    return

# this function writes all the new car coordinates in the txt file
# and then clears the list
def write_right_clicks():
    global idx_y, cars_list
    print("write to file")
    clicks_file.write("\nRow "+ str(idx_y) + " of the image:\n")
    for car in cars_list:
        clicks_file.write(str(car[0]) + ", " + str(car[1]) + "\n")
    cars_list = list()


#set mouse callback function for window
cv2.setMouseCallback(window, capture_event)

# main loop, runs until the last segment is treated or ESC is pressed
while True:
    cv2.imshow(window, np_img_segment)
    k = cv2.waitKey(1)
    if k == 13:         # enter
        next_image()
        if is_done: break
    if k == 27: break   # esc
    if is_done: break

cv2.destroyAllWindows()
clicks_file.close()

# save and display the groundtruth
cv2.imwrite(file_path+"/Groundtruths/groundtruth_"+image_name, GROUND_TRUTH_full)
cv2.imshow("Ground truth", GROUND_TRUTH_full*255)
cv2.waitKey(0)

# delete the wrong right clicks (those that were removed)
clicks_file = open(cars_file_name, "r")
lines = clicks_file.readlines()
clicks_corrected_file = open(cars_file_name, "w")

coords = []
i = 0
nb_wrong_clicks = 0
while i < len(lines):
    if lines[i][0] in str([0,1,2,3,4,5,6,7,8,9]):
        line_int = [eval(i) for i in lines[i].replace("\n", "").split(", ")]
        # only keep the coordinate if the corresponding region was marked as car
        if GROUND_TRUTH_full[line_int[1], line_int[0]]:
            coords.append(line_int)
            clicks_corrected_file.write(lines[i])
        else:
            nb_wrong_clicks+=1
    else:
        clicks_corrected_file.write(lines[i])
    i+=1

print("deleted ", nb_wrong_clicks, " wrong clicks.")
clicks_corrected_file.close()