#!/usr/bin/env python  
# coding: utf-8 
import cv2
import numpy as np
import imutils
import RPi.GPIO as GPIO  
import time 
import sys
import atexit

image = cv2.imread("/home/pi/1.jpg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_red = np.array([20, 20, 20])
upper_red = np.array([200, 200, 200])
    # mask -> 1 channel
mask = cv2.inRange(hsv, lower_red, upper_red) 
#cv2.imshow("Img", np.hstack([frame, output]))
