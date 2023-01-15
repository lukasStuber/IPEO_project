# IPEO 2022 Project Submission

## Evaluation Repository

Github: https://github.com/lukasStuber/IPEO_project.git
Google Drive: https://drive.google.com/drive/u/1/folders/1PROlh25lPq1oKjNDhKgUPj0nNGzoF-8_

## evaluation.jpynb

# install requirements
Install all the libraries in the requirements.txt file

pip install -r requirements.txt

For information on how the file works, see the text blocks in evaluation.jpynb.
By default the evaluation.jpynb file uses small images. Uncomment the corresponding sections to use medium or large images (see the text block in the jupyter notebook)

The Github repository contains everything except the Data_images and Segmentation
Download the content of Data_images and Segmentation from the Google Drive


## Groundtruth_generation.py
If you want to use the groundtruth_generation.py file, the libraries from evaluation.jpynb are enough.
The evaluation.jpynb file runs without the Groundtruth_generation.py file.

This file opens a .tif image and calculates a segmentation using the SLIC algorithm
from skimage. It displays the image in small segments to the user. It lets the user
click on the image, colorizes the clicked region and saves the clicked coordinate. 
A right click marks the region, a left click resets it to original. Pressing ENTER
loads the next segment of the image, pressing ESC ends the program.

Produces:
 - A .tif ground truth image, with 1 for clicked regions and 0 for all others
 - A .tif segmentation image, where every pixel contains the number of its region
 - A .txt file containing all the coordinates of the clicked pixels