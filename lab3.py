import serial.tools.list_ports
from uart.utils import *
from ada.utils import *
from ai.utils import *

while True:
	mess = readSerial()
	for i in range(0, len(mess), 2):
		if mess[i] in ('nhiet_do', 'anh_sang'):
			client.publish(mess[i], mess[i+1])

	time.sleep(1)

counter_ai = 3
counter_publish = 2
counter_sensor = 2
counter_anhsang = 7
i = 0
while True:
	# Cam bien
	i = (i+1)%3
	if counter_publish == 0: 
		client.publish(f'cambien{i+1}', random.randint(0,10))
		counter_publish = 5
	
	# AI
	if counter_ai == 0:
		image_capture()
		new_state = int(image_detector()[0])
		client.publish('detect_mask', new_state)
		counter_ai = 5

	# Nhiet do,  do am, anh sang
	if counter_anhsang == 0:
		mess = readSerial()
		for i in range(0, len(mess), 2):
			if mess[i] in ('nhiet_do', 'anh_sang'):
				client.publish(mess[i], mess[i+1])
		counter_anhsang = 7

	# Decrease counter
	counter_ai -= 1
	counter_publish -= 1
	counter_anhsang -= 1
	counter_sensor -= 1
	time.sleep(1)