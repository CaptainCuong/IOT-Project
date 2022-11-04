from ai.utils import *
from uart.utils import *
from ada.utils import client
import random

def publish_randint(feed_name):
	assert type(feed_name) is str, 'Feed name is not string'
	client.publish(feed_name, random.randint(0,10))

def publish_AI():
	image_capture()
	new_state = int(image_detector()[0])
	client.publish('detect_mask', new_state)

def publish_light_hum_temp():
	uart_mess = readSerial()
	if uart_mess:
		print('Update environment:')
		print(uart_mess)
		print('-'*50)
		for i in range(0, len(uart_mess), 2):
			if uart_mess[i] in ('nhiet_do', 'anh_sang'):
				client.publish(uart_mess[i], uart_mess[i+1])

def publish_uart():
	uart_mess = readSerial()
	if uart_mess:
		print('Update UART:')
		print(uart_mess)
		print('-'*50)
		for i in range(0, len(uart_mess), 2):
			if uart_mess[i] in ('nhiet_do', 'anh_sang', 'cambien1', 'cambien2', 'cambien3'):
				client.publish(uart_mess[i], uart_mess[i+1])