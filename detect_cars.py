from PIL import Image
from skimage.io import imsave, imread
from skimage.segmentation import slic
import os
import matplotlib.pyplot as plt
import numpy as np


os.chdir('C:\\Users\\lukas\\Documents\\_EPFL\\Image Processing\\Project')
path = os.getcwd()

image = imread(path + '\\swissimage_cropped2.tif')
#plt.imshow(image)

#seg_img = slic(image, n_segments=1000)
