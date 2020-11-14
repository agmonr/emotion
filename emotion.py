#!/usr/bin/env python
# pylint: disable=no-member
import cv2
import random
import sys
import numpy as np

cap = cv2.VideoCapture(0)

width = 1920
height = 1080
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


class Emotion(object):
    def __init__(self):
        
        self.frame_before = []
        self.frame_before1 = []
        self.frame = np.zeros(shape=[512, 512, 3], dtype=np.uint8)

        self.FunCount = 0 #direction of moving using s and x
        self.FunDirection=0
        self.FuncDelay=0



        self.black = None
        self.FunCount=0

        self.capture()
        self.show()

    def key_action(self):
        Key=cv2.waitKey(1)

        if Key & 0xFF == ord('q'):
            sys.exit(0)

        if Key & 0xFF == 81: #key left
            self.FunCount=self.FunCount+1
            self.FunDirection=0
            
        if Key & 0xFF == 83: #key right
            self.FunCount=self.FunCount-1
            self.FunDirection=0
            
        if Key & 0xFF == 82: #key up
            if self.FunDirection ==0:
                self.FunDirection=1
            else:
                self.FunDirection=0

        print (Key & 0xFF)

        if Key & 0xFF == 84: #key down
            if self.FunDirection==0:
                self.FunDirection=-1
            else:
                self.FunDirection=0
            
            
       
        if self.FuncDelay>20:
            self.FunCount=self.FunCount+self.FunDirection
            self.FuncDelay=0
            
        self.FuncDelay=self.FuncDelay+1
                   
        if self.FunCount>14:
            self.FunCount=0
                 
        if self.FunCount<0:
            self.FunCount=14


#       

    def capture(self):
        'Get an image.'
        _, self.img = cap.read()
        
        if self.frame_before != []:
            self.ColorMotion(self.FunCount)
            
        self.frame_before = self.img
        self.frame_before1 = self.frame_before
        self.frame_before2 = self.frame_before1

    
    def ColorMotion(self, effectId):

        if effectId == 0:  
            self.frame=100-((self.frame_before-(self.img*2-self.frame_before2))*5)
            
        if effectId == 1:  
            self.frame = self.frame_before- ((cv2.addWeighted(self.img, 0.48, self.frame_before, 0.45, 0)))
 
        if effectId == 2:  
            self.frame = self.frame_before- ((
            cv2.addWeighted(self.img, 0.48, self.frame_before2, 0.45, 0)*cv2.addWeighted(self.img, 0.50, self.frame_before1, 0.45, 0)))
            
        if effectId == 3:  
            self.frame = self.frame_before- ((
            cv2.addWeighted(self.img, 0.48, self.frame_before2, 0.45, 0)*5))

        if effectId == 4:  
            self.frame = self.frame_before- ((
            cv2.addWeighted(self.img, 0.48, self.frame_before2, 0.45, 0)^cv2.addWeighted(self.frame_before1, 0.50, self.img, 0.45, 0)))
    
        if effectId == 5:  
            self.frame = self.frame_before1- ((
            cv2.addWeighted(self.img, 0.48, self.frame_before2, 0.45, 0)))        

        if effectId == 6:  
            self.frame = self.img*2- ((
            cv2.addWeighted(self.img, 0.7, self.frame_before2, 0.5, 0) -
            self.frame_before)).clip(120, 240)

        if effectId == 7:  
            self.frame = ((
            self.img-cv2.addWeighted(self.img, 0.8, self.frame_before, 1, -5) -
            self.frame_before2))

        if effectId == 8:  
            self.frame = ((
            self.img-cv2.addWeighted(self.img, 2, self.frame_before2, 5, 2) -
            self.frame_before2)).clip(20,150)
       
        if effectId == 9:  
            bright=self.img.clip(200,255)
            self.frame = bright-(( 
            cv2.addWeighted(self.img, 1, self.frame_before2, 1, 10,) -
            self.frame_before)).clip(50,200)
 	

        if effectId == 10:  
            self.black=self.img.clip(0,0)
            self.frame = self.black-((
            cv2.addWeighted(self.img, 0.6, self.frame_before, 0.1, 0) -
            self.frame_before2))
   
        if effectId == 11:  
            self.black=self.img.clip(0,0)
            self.frame = self.black- (( 
            cv2.addWeighted(self.img, 0.8, self.frame_before2, 0.3, 0) -
            self.frame_before)).clip(0,250)

        if effectId == 12:  
            self.black=self.img.clip(0,0)
            self.frame = self.black-(self.img- ((
            cv2.addWeighted(self.img, 0.7, self.frame_before2, 0.5, 0) -
            self.frame_before)).clip(120, 240))


        if effectId == 13:  
            self.frame = (( self.img+cv2.addWeighted(self.img, 0.1, self.frame_before, 0.1, 60) - self.frame_before2 ).clip(0,60)-40 )

        if effectId == 14:  
            self.frame = self.frame_before2- ((
            cv2.addWeighted(self.img, 0.48, self.frame_before, 0.45, 0)))

        
    

    def show(self):
        'Show the motion.'
        while True:
            self.capture()
            imS = cv2.resize(self.frame, (1920, 1024))
            ims = cv2.flip(imS, 1)
            cv2.namedWindow('Frame', cv2.WINDOW_FREERATIO)
            cv2.setWindowProperty('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow("Frame", ims)
            self.key_action()
            
        self.cap.release()
        cv2.destroyAllWindows()


Emotion()
