import numpy as np
import cv2

class AustraliaMode:
	def process(frame, delta):
		frame = cv2.flip(frame, 1) 
		frame = cv2.flip(frame, 0) 
		return frame