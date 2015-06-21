#!/usr/bin/env python
# pylint: disable=no-member
'Motion visualization.'
import cv2
import random

class Emotion(object):
    'This is a mega class that does everything. Considered harmful.'

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.frame_before = []
        self.black = None

	self.Methods=[self.Psyc01,self.Psyc02,self.Psyc03,self.Psyc031,self.Psyc032,self.Psyc04,self.Psyc05,self.Psyc06,self.Psyc07]
	self.Por=8
	print self.Methods[self.Por]
        self.capture()
        self.show()

    def capture(self):
        'Get an image.'
        _, self.img = self.cap.read()

	
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
	#self.frame=self.img-self.frame_before

	

    def show(self):
        'Show the motion.'
        while True:
            self.capture()
            cv2.namedWindow("Frame", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty(
                "Frame", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
            self.frmae = cv2.flip(self.frame, 0)
            cv2.imshow("Frame", self.frame)

            if cv2.waitKey(1) & 0xFF == ord('a'):
		self.Por=self.Por+1
		if self.Por>=len(self.Methods):
			self.Por=0
		
		print str(self.Por)+"==="+str(self.Methods[self.Por])

        self.cap.release()
        cv2.destroyAllWindows()


Emotion()
