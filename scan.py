# Import the necessary packages
import argparse

import cv2
import imutils
import numpy as np
from skimage.filters import threshold_local

from pyimagesearch.transform import four_point_transform
