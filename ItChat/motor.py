#!/usr/bin/env python  
# coding: utf-8  
 
import RPi.GPIO as GPIO  
import time 
import sys

def tonum(num):
    fm=10.0/180.0
    num=num*fm+2.5
    num=int(num*10)/10.0
    return num

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
P21 = GPIO.PWM(21,50)
P21.start(tonum(0))
P23 = GPIO.PWM(23,50)
P23.start(tonum(0))

P21.ChangeDutyCycle(tonum(int(sys.argv[2])))
P23.ChangeDutyCycle(tonum(int(sys.argv[1])))
time.sleep(0.3)

