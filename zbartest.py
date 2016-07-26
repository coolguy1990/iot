#!/usr/bin/env python

# Python 3 compat
from __future__ import print_function
try:
    input = raw_input
except NameError:
    pass


import time
# import picamera
# import picamera.array
import cv2
import numpy as np
import zbar

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
camera.set(cv2.CAP_PROP_FPS, 24)

while True:

    (grabbed, frame) = camera.read()
    yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    scanner = zbar.ImageScanner()

    arrays = np.array(frame)

    image = zbar.Image(1280, 720, 'Y800', arrays.tostring())

    print(image)
    
    scanner.parse_config('enable')
    scanner.scan(image)
    for symbol in image:
        print(symbol.type, symbol.data)


# with picamera.PiCamera() as camera:

    # camera.resolution = (1280, 720)
    # camera.framerate = 24
    # camera.start_preview()
    # # Wait for the user to press Enter before capturing something
    # input()
    # with picamera.array.PiYUVArray(camera) as stream:
    #     camera.capture(stream, format='yuv')
    #     # Now stream.array is a numpy array containing YUV image data.
    #     # zbar's Image class wants stuff in "Y800" format which just
    #     # means the Y plane (0) of this data.
    #     image = zbar.Image(1280, 720, 'Y800', stream.array[..., 0].tostring())
    #     # Finally, get zbar to scan it...
    #     scanner = zbar.ImageScanner()
    #     scanner.parse_config('enable')
    #     scanner.scan(image)
    #     for symbol in image:
    #         print(symbol.type, symbol.data)