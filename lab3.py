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