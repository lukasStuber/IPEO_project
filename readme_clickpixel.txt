click_pixel.py

created by: Lukas Stuber
date: 25 Nov 2022
Requirements: numpy, skimage, opencv

This file opens a .tif image and calculates a segmentation using the SLIC algorithm
from skimage. It displays the image in small segments to the user. It lets the user
click on the image, colorizes the clicked region and saves the clicked coordinate. 
A right click marks the region, a left click resets it to original. Pressing ENTER
loads the next segment of the image, pressing ESC ends the program.

Produces:
 - A .tif ground truth image, with 1 for clicked regions and 0 for all others
 - A .tif segmentation image, where every pixel contains the number of its region
 - A .txt file containing all the coordinates of the clicked pixels