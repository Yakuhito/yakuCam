import cv2
import pyfakewebcam
import numpy as np
import time
import threading

import video_modes as vmodes

quit = False
modes = vmodes.modes
selected_mode = 0
current_mode_start_time = time.time()

def video_processing_thread():
	global quit
	global modes
	global selected_mode
	global current_mode_start_time

	cap = cv2.VideoCapture('/dev/video0')

	height, width = 720, 1280
	cap.set(cv2.CAP_PROP_FRAME_WIDTH ,width)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
	cap.set(cv2.CAP_PROP_FPS, 30)

	fake = pyfakewebcam.FakeWebcam('/dev/video20', width, height)

	while not quit:
		success, frame = cap.read()
		if not success:
			print('Error while reading frame :(')
			continue
		img_out = modes[selected_mode][1].process(frame, time.time() - current_mode_start_time)

		cv2.imshow('Preview', img_out)
		img_out = cv2.cvtColor(img_out, cv2.COLOR_BGR2RGB)
		fake.schedule_frame(img_out)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			quit = True


	cap.release()
	cv2.destroyAllWindows()


def mode_selection_thread():
	global quit
	global modes
	global selected_mode
	global current_mode_start_time

	while not quit:
		print('AVAILABLE MODES (FILTERS)')
		print('-------------------------')
		for i in range(len(modes)):
			print(str(i) + '. ' + modes[i][0])
		print('q. quit')
		print('')
		selection = input('Choice: ')
		print('')
		print('')
		if selection == 'q':
			quit = True
		elif int(selection) < len(modes):
			selected_mode = int(selection)
			current_mode_start_time = time.time()


def main():
	t1 = threading.Thread(target=mode_selection_thread, args=())
	t2 = threading.Thread(target=video_processing_thread, args=())

	t1.start()
	t2.start()

if __name__ == "__main__":
	main()