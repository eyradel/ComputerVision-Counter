# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 19:19:18 2022

@author: Delaeyram
"""

#AUTHOR KUWORNU EYRAM DELA 
import cv2
import time
import cvlib as cv
#import pyttsx3
import pyfirmata
pin = 9
pin1 = 10
buzzer = 7
port = "COM3"
board = pyfirmata.Arduino(port)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output=cv2.VideoWriter('scarecrow.mp4',fourcc,20.0,(640,480))
output_heat=cv2.VideoWriter('scarecrowheat.mp4',fourcc,20.0,(640,480))
from cvlib.object_detection import draw_bbox
im = cv2.VideoCapture(r"C:\Users\Delaeyram\Desktop\bird\birds.mp4")


while True:
    success,cap = im.read()
    cv2.imshow("output",cap)
    bbox, label, conf = cv.detect_common_objects(cap)
    output_image = draw_bbox(cap, bbox, label, conf)
    hsv = cv2.cvtColor(output_image,cv2.COLOR_BGR2HSV)
    cv2.imshow("output",output_image)
    if "bird" in label:
        print("Bird Detected")
        board.digital[pin].write(0)
        board.digital[pin1].write(1)
        board.digital[buzzer].write(1)
        
    else:
        board.digital[pin].write(1)
        board.digital[pin1].write(0)
        board.digital[buzzer].write(0)
        
        
        
    cv2.imshow("Heat",hsv)
    output.write(output_image)
    output_heat.write(hsv)
    #print(str(label))
    #print("number of bird  = ",label.count('bird'))
    
        

    
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

im.release()
cv2.destroyAllWindows()
