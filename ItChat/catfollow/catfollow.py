#from gpiozero import Motor
#from time import sleep
#!/usr/bin/env python  
# coding: utf-8 
import cv2
import numpy as np
import imutils
import RPi.GPIO as GPIO  
import time 
import sys
import atexit
import os

#m = Motor(forward=17, backward=18) # fwd=cw bck=ccw

def tonum(num):
    fm=10.0/180.0
    num=num*fm+2.5
    num=int(num*10)/10.0
    return num

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
P21 = GPIO.PWM(21,50)
#P21.start(tonum(0))
P23 = GPIO.PWM(23,50)
P23.start(tonum(90))
print("start")

if __name__ == '__main__':
    
    cap = cv2.VideoCapture(0)
    #boundaries = [ ( [160, 20, 20],    #lower color range
                # [179, 255, 255] ) ]#upper color range
    while True:
        
        #EXTRACT_FOLDER = '/home/pi/ItChat/extract_folder'
        #save_path = "/home/pi/ItChat/extract_folder/2.jpg"
        
        ret, frame = cap.read()
        #cv2.imwrite(save_path, frame)
        #Img = cv2.imread("/home/pi/ItChat/extract_folder/2.jpg")
        #print(type(Img))
        #print(type(frame)) 
    #Img = cv2.imread('/home/pi/1.jpg')#
        #kernel_2 = np.ones((2,2),np.uint8)#
        #kernel_3 = np.ones((3,3),np.uint8)#
        #kernel_4 = np.ones((4,4),np.uint8)#

##cv2.imwrite("/media/pi/USB1/yellowBALL.jpg", frame)
    #if Img is not None:#
        #for (lower,upper) in boundaries:
            #lower = np.array(lower,dtype = "uint8")
            #upper = np.array(upper,dtype = "uint8")
        #Lower = np.array([160, 20, 20])
        #Upper = np.array([179, 255, 255])
        lower_red = np.array([120, 20, 20])
        upper_red = np.array([179, 255, 255])
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    
        mask = cv2.inRange(gray, lower_red, upper_red)
        print(type(mask))
        
            


            
  
        #erosion = cv2.erode(mask,kernel_4,iterations = 1)
        #erosion = cv2.erode(erosion,kernel_4,iterations = 1)
        #dilation = cv2.dilate(erosion,kernel_4,iterations = 1)
        #dilation = cv2.dilate(dilation,kernel_4,iterations = 1)
  #
        #target = cv2.bitwise_and(frame, frame, mask=dilation)
  #
        ret, binary = cv2.threshold(mask.copy(),127,255,cv2.THRESH_BINARY) 
  #
        img, cnts, hierarchy = cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
        #p=0
        #cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        print("cnts=",len(cnts))
        if len(cnts) > 0: #4
            c = max(cnts, key=cv2.contourArea)
            ((x,y), radius) = cv2.minEnclosingCircle(c)
            x, y = int(x), int(y)
            print(x)
            print(y)
            print(radius)
            M = cv2.moments(c)
            #print(M)
            #center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            global Origin
            Origin = 7.5
            if radius > 10:
                cv2.circle(frame, (int(x), int(y)), int(radius), (0,255,255),2)
                #cv2.circle(Img, center, 5, (0,0,255), -1)
                x, y = int(x), int(y)
                
                #print x, y

                if x > 420 and (Origin-(x-320)/192)>0:
                    P23.ChangeDutyCycle(Origin-(x-320)/192)
                    Origin = Origin-(x-320)/192
                    #reverseRotation(self)
                    print("Origin=>",Origin)
                    time.sleep(0.3)
                    P23.ChangeDutyCycle(0)
                    #os.system("raspistill-t 1 -o test.jpg")
                    time.sleep(0.1)

                elif x <= 220 :
                    #steer.reverseRotation()
                    P23.ChangeDutyCycle(Origin-(x-320)/192)
                    Origin = Origin-(x-320)/192
                    print("Origin=<",Origin)
                    #forwardRotation(self)
                    time.sleep(0.3)
                    P23.ChangeDutyCycle(0)
                    #os.system("raspistill-t 1 -o test.jpg")
                    time.sleep(0.1)
                    
                    #Origin = 320-x+Origin
                elif 220 < x < 420 : 
                    print("It's middle")                   
                    

##                    sleep(.5)
                #elif x > 400:
                    #steer.forwardRotation()
                    #P23.ChangeDutyCycle((x-500+Origin)/180)
                   # Origin = x-500+Origin
                    #time.sleep(.04)
                    # m.stop()
##                    sleep(.5)
                #elif (x <= 100):
                   # m.backward(1)
                   # sleep(.05)
                   # m.stop()
              #  elif (x >= 520):
               #     m.forward(1)
               #     sleep(.05)
               #     m.stop()
        else:
            continue

        output = cv2.bitwise_and(frame, frame, mask = mask)

        cv2.imshow("Img", np.hstack([frame, output]))


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)

        


 
