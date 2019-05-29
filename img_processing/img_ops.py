#!/usr/bin/python3

import cv2
#import computer vision build in c++ language
# reading image data
read_ops=[i for i in dir(cv2) if 'read' in i]
print(read_ops)

#reading data from image
img=cv2.imread('cat.jpg',1) #loading original image
greying=cv2.imread('cat.jpg',0) #removing color channel
transimg=cv2.imread('cat.jpg',-1) #removing color channel

#shape and size , type
print(img.shape)
print(greying.shape)
print(img.size)
print(greying.size)
#print(type(img))
# data print of image
#print(img)
#showing image
cv2.imshow('win',img)
cv2.imshow('grey',greying)
cv2.imshow('trans',transimg)
#to hold image window
cv2.waitkey(0)
#destroying windows
cv2.destroyAllWindows()
