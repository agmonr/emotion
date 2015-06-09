import cv2
from config import *


class emotion:

	def __init__(self):
		self.cap = cv2.VideoCapture(0)
		self.frame_before=[]
		
		self.capture()
		self.show()


	def capture(self):

    		ret, img = self.cap.read()
#		img=scipy.misc.imresize(img,(100,100))
#		img=scipy.misc.imresize(img,(768,1024))
#		img= ndimage.gaussian_filter(img, sigma=8)	
		if self.frame_before != []:
#			self.frame=img	
			#self.frame=(img-self.frame_before)
			#self.frame=self.black-((cv2.addWeighted(img,0.8,self.frame_before,0.07,0)-self.frame_before)).clip(100,255)
			self.frame=self.black-((cv2.addWeighted(img,0.8,self.frame_before,0.1,0)-self.frame_before)).clip(120,255)
		else:
			self.black=img.clip(0,0)	
			#self.frame=((self.frame-self.frame_before)).clip(0,250)
			
		self.frame_before=img

	def show(self):
		while(True):
			self.capture()
			cv2.namedWindow("Frame", cv2.WINDOW_AUTOSIZE )
			r = int(long(YScreenResulation*1000 / self.frame.shape[0]*1000)) # *1000 cause we need better precision
			dim = (int(self.frame.shape[1]*r)/1000000,YScreenResulation)
			frame=cv2.resize(self.frame, dim, interpolation = cv2.INTER_AREA)
			cv2.moveWindow("Frame", int((XScreenResulation-self.frame.shape[1])/2), 0) 
			cv2.imshow("Frame",self.frame)
	
    			if cv2.waitKey(1) & 0xFF == ord('q'):
        			break

		self.cap.release()
		cv2.destroyAllWindows()


Emotion= emotion()
