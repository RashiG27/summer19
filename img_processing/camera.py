#!/usr/bin/python3

import cv2

#describing version
print(cv2.__version__)

#search for camera handling function
x=[i for i in dir(cv2) if 'Video'in i]
print(x)

#starting to capture video
cap=cv2.VideoCapture(0) # data live, stored, streamed
print(dir(cap)) #exploring camera ops

#checking camera start point
while cap.isOpened():
    status,img=cap.read()
    #changing image gray scale
    graying=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #now displaying image
    cv2.imshow('live',img)
    cv2.imshow('live1',img)
    cv2.imshow('live2',img)
    cv2.imshow('live3',img)
    cv2.imshow('gray',greyimg)
    # close window in 10ms, keyboard action capture, ord==ascii values --q
    if cv2.waitKey(10) & 0xff==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
