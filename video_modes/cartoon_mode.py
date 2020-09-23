import numpy as np
import cv2

# https://www.askaswiss.com/2016/01/how-to-create-cartoon-effect-opencv-python.html
class CartoonMode:
	def process(frame, delta):
		num_down = 2
		num_bilateral = 7
		img_rgb = frame

		# downsample image using Gaussian pyramid
		img_color = img_rgb
		for _ in range(num_down):
			img_color = cv2.pyrDown(img_color)

		# repeatedly apply small bilateral filter instead of
		# applying one large filter
		for _ in range(num_bilateral):
			img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=9, sigmaSpace=7)

		# upsample image to original size
		for _ in range(num_down):
			img_color = cv2.pyrUp(img_color)

		# convert to grayscale and apply median blur
		img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
		img_blur = cv2.medianBlur(img_gray, 7)

		img_edge = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=2)

		# convert back to color, bit-AND with color image
		img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
		img_cartoon = cv2.bitwise_and(img_color, img_edge)
		return img_cartoon
