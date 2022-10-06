from simple_ai import *
import time

counter_sensor = 5
counter_ai = 30
while True:
	time.sleep(5)
	counter_sensor = counter_sensor -1
	if counter_sensor <= 0:
		counter_sensor = 5
		client.publish("",)

	counter_ai = counter_ai -1
	if counter_ai <= 0:
		counter_ai = 30
		image_capture()
		ai_result = image_detector()
		client.publish("ai", ai_result)
	image_capture()
	image_detector()