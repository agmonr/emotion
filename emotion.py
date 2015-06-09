#!/usr/bin/env python
# pylint: disable=no-member
'Motion visualization.'
import cv2


class Emotion(object):
    'This is a mega class that does everything. Considered harmful.'

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.frame_before = []
        self.black = None

        self.capture()
        self.show()

    def capture(self):
        'Get an image.'
        _, self.img = self.cap.read()
        if self.frame_before != []:
		self.Psyc04()

        self.frame_before = self.img

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
                cv2.addWeighted(self.img, 1, self.frame_before, 1, 0) -
                self.frame_before))
	
    def Psyc04(self):
	self.black=self.img.clip(0,0)
	self.frame = self.black-((
                cv2.addWeighted(self.img, 0.6, self.frame_before, 0.1, 0) -
                self.frame_before))
	

    def show(self):
        'Show the motion.'
        while True:
            self.capture()
            cv2.namedWindow("Frame", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty(
                "Frame", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
            self.frmae = cv2.flip(self.frame, 1)
            cv2.imshow("Frame", self.frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()


Emotion()
