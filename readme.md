# IPEO 2022 Project Submission

## Evaluation Repository

Github: https://github.com/lukasStuber/IPEO_project.git
Google Drive: https://drive.google.com/drive/u/1/folders/1PROlh25lPq1oKjNDhKgUPj0nNGzoF-8_

## evaluation.ipynb
This file executes the content of the project (load the data, create features, train the random forest, evaluate, etc.)

# install requirements
Install all the libraries in the requirements.txt file

pip install -r requirements.txt

For information on how the file works, see the text blocks in evaluation.ipynb.
By default the evaluation.jpynb file uses small images. Uncomment the corresponding sections to use medium or large images (see the text block in the jupyter notebook)

The Google Drive contains everything, including very large images. It also contains the folder "unused_Data_images" with all the images that we downloaded but were not used for the Random forest.
The Github repository contains everything except the content of the "Data_images" and "Segmentation" folders. The empty folders are there but not the content because these images are too large for git.
If you want to use github, please download the content of the "Data_images" and "Segmentation" folders and place it in the git folder. The .gitignore file will ignore all the large images in these two folders.

To use the evaluation.ipynb, you can just install the packages needed, then (once you make sure that all the folders with their contents are available), you can run the whole notebook.
In case you wanted to use the code-generated-classifier, without spending time actually optimizing it, you can import the classifier in folder ARCHIVE. In such folder, there are the predictions for the small, medium and large images.
The classifier are available for the small and medium images. You can import them as shown after block "Third part: the Results" (if needed). 
Of course, for the classifier to run, the features must already be computed, and the sub-images must be calculated (see the comments in evaluation.ipynb)
In case you do not want to load the classifier, you can quickly train the classifier (takes 2s) using the optimal parameters from the report.

## Groundtruth_generation.py
If you want to use the groundtruth_generation.py file, the libraries from evaluation.ipynb are enough.
The evaluation.ipynb file runs without the Groundtruth_generation.py file.

This file opens a .tif image and calculates a segmentation using the SLIC algorithm
from skimage. It displays the image in small segments to the user. It lets the user
click on the image, colorizes the clicked region and saves the clicked coordinate. 
A right click marks the region, a left click resets it to original. Pressing ENTER
loads the next segment of the image, pressing ESC ends the program.

Produces:
 - A .tif ground truth image, with 1 for clicked regions and 0 for all others
 - A .tif segmentation image, where every pixel contains the number of its region
 - A .txt file containing all the coordinates of the clicked pixels