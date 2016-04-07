# USAGE
# python detect_barcode.py --image images/barcode_01.jpg

# import the necessary packages
import sys
import numpy as np
import argparse
import cv2
#import Image

#sys.path.append('/usr/local/lib/python2.7/dist-packages')

# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "path to the image file")
#args = vars(ap.parse_args())

#load from camera
cap = cv2.VideoCapture(0)
_,cv2_im = cap.read()

# load the image and convert it to grayscale
#image = cv2.imread(args["image"])
#gray = cv2.cvtColor(cv2_im, cv2.COLOR_BGR2GRAY)
#gray = cv2.cvtColor(cv2_im, cv2.COLOR_RGB2GRAY)


cv2.imshow("adadad", cv2_im)
cv2.waitKey(0)

# compute the Scharr gradient magnitude representation of the images
# in both the x and y direction
#gradX = cv2.Sobel(gray, ddepth = cv2.cv.CV_32F, dx = 1, dy = 0, ksize = -1)
#gradY = cv2.Sobel(gray, ddepth = cv2.cv.CV_32F, dx = 0, dy = 1, ksize = -1)
gradX = cv2.Sobel(gray, cv2.CV_16S,1,0,ksize=-1)
gradY = cv2.Sobel(gray, cv2.CV_16S,0,1,ksize=-1)

# subtract the y-gradient from the x-gradient
gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient,1,1)

# blur and threshold the image
blurred = cv2.blur(gradient, (20, 20))
(_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)

# construct a closing kernel and apply it to the thresholded image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# perform a series of erosions and dilations
closed = cv2.erode(closed, None, iterations = 4)
closed = cv2.dilate(closed, None, iterations = 4)

# find the contours in the thresholded image, then sort the contours
# by their area, keeping only the largest one
(_, cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
c = sorted(cnts, key = cv2.contourArea, reverse = True)[0]

# compute the rotated bounding box of the largest contour
rect = cv2.minAreaRect(c)
box = np.int0(cv2.boxPoints(rect))

# draw a bounding box arounded the detected barcode and display the
# image
cv2.drawContours(image, [box], -1, (0, 255, 0), 4)
#cv2.imshow("Image", thresh)
#cv2.imshow("Image2", image)

#processing thru zbar
#image = image.convert('L')

#cv2.imshow("Image", image)





cv2.waitKey(0)
