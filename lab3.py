import serial.tools.list_ports
from task.task import *

counter_ai = 3
counter_publish = 2
counter_sensor = 2
counter_anhsang = 7
i = 0
while True:
	# Cam bien
	i = (i+1)%3
	if counter_publish == 0: 
		publish_randint(f'cambien{i+1}')
		counter_publish = 5
	
	# AI
	if counter_ai == 0:
		publish_AI()
		counter_ai = 5

	# Nhiet do,  do am, anh sang
	if counter_anhsang == 0:
		publish_light_hum_temp()
		counter_anhsang = 7

	# Decrease counter
	counter_ai -= 1
	counter_publish -= 1
	counter_anhsang -= 1
	counter_sensor -= 1
	time.sleep(1)
	