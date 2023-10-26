import cv2
import os
import numpy as np
from tensorflow.keras import models
capture = cv2.VideoCapture(0)

#model = models.load_model('model_Msize.h5')
model = models.load_model('model_Lsize.h5')

list = ["長手", "短手"]


print("-- usage --")
print("Shot: Space")
print("Quit: q")
print("-- info --")
print("cam_WIDTH: " + str(capture.get(3)))
print("cam_HEIGHT: " + str(capture.get(4)))

frame_width = int(capture.get(3))
frame_height = int(capture.get(4))
set_width = 60
set_height = 150

count = 0
while True:
	ret, frame = capture.read()
	frame = frame[0:frame_height, int(frame_width / 2 - frame_height * set_width / (2 * set_height))\
	:int(frame_width /2 + frame_height * set_width /( 2 * set_height))]
	cv2.imshow('CAM', frame)
	key = cv2.waitKey(1)
	if key == ord('q'):
		break
	elif key == ord(' '):
		frame = cv2.resize(frame, dsize = (60, 150))
		#cv2.imshow('predict'.frame)
		frame = (np.expand_dims(np.array(frame)/255,0))
		predictions = model.predict(frame)
		result = list[np.argmax(predictions)]
		print("予測結果は", result, "です。", predictions)
		print("次に進むにはなにかボタンを押してください")
		print()
		key = cv2.waitKey(0)

capture.release()
cv2.destroyAllWindows