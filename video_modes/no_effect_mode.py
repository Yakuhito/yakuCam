import numpy as np
import cv2

class NoEffectMode:
	def process(frame, delta):
		return frame
