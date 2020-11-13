#!/usr/bin/env python
# pylint: disable=no-member
import cv2
import random
import numpy as np

cap = cv2.VideoCapture(0)

width = 1920
height = 1080
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


class Emotion(object):
    def __init__(self):
        
        self.frame_before = []
        self.frame = np.zeros(shape=[512, 512, 3], dtype=np.uint8)
        self.black = None
        self.Methods=[self.Psyc01,self.Psyc02,self.Psyc03,self.Psyc031,self.Psyc032,self.Psyc04,self.Psyc05,self.Psyc06,self.Psyc07,self.Psyc08]
        self.Por=0
        print (self.Methods[self.Por])
        self.capture()
        self.show()

    def capture(self):
        'Get an image.'
        _, self.img = cap.read()
        
        if self.frame_before != []:
            
            self.Master(self.Methods[self.Por])
        self.frame_before = self.img

    def Master(self,methodToRun):
    	result = methodToRun()


    def Psyc01(self):
        self.frame = self.frame_before- ((
            cv2.addWeighted(self.img, 0.7, self.frame_before, 0.5, 0) -
            self.frame_before)).clip(120, 240)
        
	
    def Psyc02(self):
        self.frame = self.img*2- ((
                cv2.addWeighted(self.img, 0.7, self.frame_before, 0.5, 0) -
                self.frame_before)).clip(120, 240)

    def Psyc03(self):
        self.frame = ((
                cv2.addWeighted(self.img, 1, self.frame_before, 1, 0,) -
                self.frame_before))
    
    def Psyc031(self):
        self.frame = ((
                cv2.addWeighted(self.img, -5, self.frame_before, -1, 10) -
                self.frame_before)).clip(0,250)
    
    def Psyc032(self):
        bright=self.img.clip(200,255)
        self.frame = bright-(( 
                cv2.addWeighted(self.img, 1, self.frame_before, 1, 10,) -
                self.frame_before)).clip(50,200)
 	
    def Psyc04(self):
        self.black=self.img.clip(0,0)
        self.frame = self.black-((
                cv2.addWeighted(self.img, 0.6, self.frame_before, 0.1, 0) -
                self.frame_before))

    def Psyc05(self):
        self.black=self.img.clip(0,0)
        self.frame = self.black- (( 
                cv2.addWeighted(self.img, 0.8, self.frame_before, 0.3, 0) -
                self.frame_before)).clip(0,250)

    def Psyc06(self):
        self.black=self.img.clip(0,0)
        self.frame = self.black-(self.img- ((
                cv2.addWeighted(self.img, 0.7, self.frame_before, 0.5, 0) -
                self.frame_before)).clip(120, 240))

    def Psyc07(self):
        self.frame = (( self.img+cv2.addWeighted(self.img, 0.1, self.frame_before, 0.1, 60) - self.frame_before ).clip(0,60)-40 )
        print ('x')
        

    def Psyc08(self):
        rows=1920
        cols=1080
        for i in range(rows):
            for j in range(cols):
                k = self.img_before[i,j]
                print (k)
        
        
        


    def key_action(self):
        Key=cv2.waitKey(1)

        if Key & 0xFF == ord('q'):
            sys.exit

        if Key & 0xFF == ord('a'):
            self.Por=self.Por+1
            print (self.Por)

        if Key & 0xFF == ord('z'):
            self.Por=self.Por-1
            print (self.Por)

        if self.Por>=len(self.Methods):
            self.Por=0

        if self.Por<0:
            self.Por-len(self.Methods)


    def show(self):
        'Show the motion.'
        while True:
            self.capture()
            imS = cv2.resize(self.frame, (1920, 1024))   
            cv2.imshow("Frame", imS)
            self.key_action()
            
        self.cap.release()
        cv2.destroyAllWindows()


Emotion()
