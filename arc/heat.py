# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 20:26:57 2021

@author: EyraDel
"""
import numpy as np
import cv2 as cv
import time
import psutil
# import pyttsx3
from random import randint


        

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)
plugged = "Plugged In" if plugged else "Not Plugged In"
# engine = pyttsx3.init()
# voice = engine.getProperty('voices')
# engine.setProperty('voice',voice[1].id)
# rate = engine.getProperty('rate')
# engine.setProperty("rate", 120)
# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
    
# speak("object detection and tracking system running please wait")

try:
    data = open('Data.txt',"w")
except:
    print( "file not found")


cnt_up   = 0
cnt_down = 0



cap = cv.VideoCapture(r"C:\Users\kuwor\Downloads\Video\Birds Flying in Slow Motion - Red Kite Bird Extravaganza.mp4")
# address = "http://192.168.43.63:8080/video"
# cap.open(address)


fgbg = cv.createBackgroundSubtractorMOG2(detectShadows = True)


kernelOp = np.ones((3,3),np.uint8)
kernelOp2 = np.ones((5,5),np.uint8)
kernelCl = np.ones((11,11),np.uint8)


font = cv.FONT_HERSHEY_SIMPLEX
persons = []


while(cap.isOpened()):

 
    ret, frame = cap.read()


    for i in persons:
        i.age_one() 
    fgmask = fgbg.apply(frame)
    fgmask2 = fgbg.apply(frame)

   
    try:
        ret,imBin= cv.threshold(fgmask,200,255,cv.THRESH_BINARY)
        ret,imBin2 = cv.threshold(fgmask2,200,255,cv.THRESH_BINARY)
      
        mask = cv.morphologyEx(imBin, cv.MORPH_OPEN, kernelOp)
        mask2 = cv.morphologyEx(imBin2, cv.MORPH_OPEN, kernelOp)
       
        mask =  cv.morphologyEx(mask , cv.MORPH_CLOSE, kernelCl)
        mask2 = cv.morphologyEx(mask2, cv.MORPH_CLOSE, kernelCl)
    except:
        print('EOF')
        print( 'UP:',cnt_up)
        print ('DOWN:',cnt_down)
        break
  
    contours0, hierarchy = cv.findContours(mask2,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours0:
        area = cv.contourArea(cnt)
       

    total = cnt_down+cnt_up
    str_up = 'UP: '+ str(cnt_up)
    str_down = 'DOWN: '+ str(cnt_down)
   
    imggray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    
  
    cv.imshow('Mask',cv.resize(mask,(480,480)))  
    cv.imshow('heat',cv.resize(hsv,(480,480)))
    


    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
# speak(f" movement {str_up}")
# speak(f"  movement {str_down}")
# speak(f"total number of people{total}")
data.flush()
data.close()
cap.release()
cv.destroyAllWindows()
