# -*- coding: UTF-8 -*-
import cv2
import os
import time
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import uploadFile
c=uploadFile.Client()
camera=cv2.VideoCapture(1)
camera2=cv2.VideoCapture(2)
cascader=cv2.CascadeClassifier("Client"+os.path.sep+"haarcascade_frontalface_default.xml")
while True:
    ret,frame=camera.read()
    ret,frame2=camera2.read()
    if not ret:
        break
    choose=cv2.waitKey(1)
    img=Image.fromarray(frame)
    if choose==ord('q'):
        break
    elif choose==ord('g'):
        #检测到用户输入 准备人脸识别取车
        '''
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        rect=cascader.detectMultiScale(gray,1.3,5)
        for x,y,w,h in rect:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),10)
            pass'''
        cv2.imwrite("tmp.jpg",frame2)
        ret=c.sendFile("tmp.jpg",True)
        if ret!="NULL":
            #w,h=frame.shape[:2]
            #draw=ImageDraw.Draw(img)
            #ttf = ImageFont.load_default()
            #draw.text((int(w/2), int(h/2)),"已找到你的汽车："+ret,(255, 0, 0),font=ttf)
            #cv2.putText(frame, "已找到你的汽车："+ret, (int(w/2), int(h/2)), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 0))
            #绘制结果
            print("已找到你的汽车："+ret)
            pass
        input()
        pass#end elif choose==ord('g'):
    cv2.imwrite("tmp.jpg",frame)
    w,h=frame.shape[:2]
    ret=c.sendFile("tmp.jpg",False)
    if ret!="NULL":
        #w,h=frame.shape[:2]
        #draw=ImageDraw.Draw(img)
        #ttf = ImageFont.load_default()
        #draw.text((int(w/2), int(h/2)),ret+" 当前时间"+time.ctime(),(255, 0, 0),font=ttf)
        #cv2.putText(frame, ret+" 当前时间"+time.ctime(), (int(w/2), int(h/2)), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, ))
        print(ret+" 当前时间"+time.ctime())
        '''
        if ret.find("8")!=-1 or ret.find("5")!=-1 or ret.find("V")!=-1:
            #苏E 05EV8
            cv2.putText(frame, "苏E05EV8 当前时间"+time.ctime(), (int(w/2), h), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, ))
            pass
        elif ret.find("A")!=-1 or ret.find("1")!=-1 or ret.find("2")!=-1:
            cv2.putText(frame, "辽A0AE12 当前时间"+time.ctime(), (int(w/2), h), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, ))
            pass'''
        pass
    #cv2.imshow("camera",np.array(img))
    cv2.imshow("camera",frame)
    cv2.imshow("camera2",frame2)
    pass
camera.release()
cv2.destroyAllWindows()