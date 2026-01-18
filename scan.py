# Import the necessary packages
import argparse

import cv2
import imutils
import numpy as np
from skimage.filters import threshold_local

from pyimagesearch.transform import four_point_transform

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image being scanned")
args = vars(ap.parse_args)
