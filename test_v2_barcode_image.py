# import the necessary packages
import numpy as np
import cv2
import argparse
import zbar
from PIL import Image
from barcodescanner.barcodedetect import barcodedetect

detect = barcodedetect()

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to the image file")
args = vars(ap.parse_args())

# 	# detect the barcode in the image
image = cv2.imread(args["image"])
box = detect.detect(image)

# if a barcode was found, draw a bounding box on the frame
cv2.drawContours(image, [box], -1, (0, 255, 0), 2)

# process the barcode with zbar


# show the frame and record if the user presses a key
cv2.imshow('Image', image)
cv2.waitKey(0)

# cleanup the camera and close any open windows
cv2.destroyAllWindows()