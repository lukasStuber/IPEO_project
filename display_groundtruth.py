import cv2
import numpy as np
import os
import string

# get the path of the image
file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(file_path)
#image_name = 'swissimage_cropped2.tif'
image_name = 'swissimage-dop10_2022_2682-1249_0.1_2056.tif'
path_image = file_path + '/Data_images/' + image_name

groundtruth = np.array(cv2.imread(file_path+"/Groundtruths/groundtruth.tif", cv2.IMREAD_GRAYSCALE), np.uint8).T
cv2.imshow("Ground truth", groundtruth*255)
cv2.waitKey(0)

clicks_file = open("./Groundtruths/cars.txt", "r+")
lines = clicks_file.readlines()
clicks_file.close()

clicks_corrected_file = open("./Groundtruths/cars.txt", "w")

coords = []
i = 0
nb_wrong_clicks = 0
while i < len(lines):
    if lines[i][0] in str([0,1,2,3,4,5,6,7,8,9]):
        line_int = [eval(i) for i in lines[i].replace("\n", "").split(", ")]
        if groundtruth[line_int[0], line_int[1]]:
            coords.append(line_int)
            clicks_corrected_file.write(lines[i])
        else:
            nb_wrong_clicks+=1
    else:
        clicks_corrected_file.write(lines[i])
    i+=1

print(nb_wrong_clicks)
clicks_corrected_file.close()