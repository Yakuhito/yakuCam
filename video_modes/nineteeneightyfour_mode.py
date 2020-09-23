import numpy as np
import cv2

# I do know how to spell Nineteen Eighty-Four,
# but I left it like this for the haters
class NineteeneightyfourMode:
	def process(frame, delta):
		frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
		frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
		return frame
