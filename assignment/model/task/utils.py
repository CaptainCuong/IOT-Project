from ..ai.utils import *
from ..uart.utils import *
from ..ada.utils import client

def publish(obj):
	if len(obj.buffer) > 0:
		feed, mess = obj.buffer[0]
		client.publish(feed, mess)
		obj.buffer = obj.buffer[1:]

def update_state(obj):
	if obj.state == 0:
		if len(obj.buffer) > 0:
			print(f'Change to state 1')
			obj.state = 1
	elif obj.state == 1:
		print('Change to state 2')
		client.receive_ack = False
		publish(obj)
		obj.state = 2
	elif obj.state == 2:
		if obj.failures >= 4:
			print('Change to state 3')
			obj.state = 3
		elif not client.receive_ack:
			print('Change to state 1')
			obj.state = 1
			obj.failures += 1
		elif client.receive_ack:
			print('Change to state 0')
			obj.state = 0
			obj.failures = 0
		else:
			raise	
	elif obj.state == 3:
		raise Exception('Connection Error')
	else:
		pass

def publish_AI(obj):
	image_capture()
	new_state = int(image_detector()[0])
	obj.buffer.append(('detect_mask', new_state))
	return new_state

def publish_light_hum_temp(obj):
	uart_mess = readSerial()
	if uart_mess:
		print('Update environment:')
		print(uart_mess)
		print('-'*50)
		for mess in uart_mess:
			if mess[1] == 'H':
				obj.buffer.append(('do_am', mess[2]))
			elif mess[1] == 'T':
				obj.buffer.append(('nhiet_do', mess[2]))
			elif mess[1] == 'L':
				obj.buffer.append(('anh_sang', mess[2]))
	return uart_mess

# def publish_uart():
# 	uart_mess = readSerial()
# 	if uart_mess:
# 		print('Update UART:')
# 		print(uart_mess)
# 		print('-'*50)
# 		for i in range(0, len(uart_mess), 2):
# 			if uart_mess[i] in ('nhiet_do', 'anh_sang', 'cambien1', 'cambien2', 
# 								'cambien3', 'received_mess', 'nutnhan1', 'nutnhan2'):
# 				client.publish(uart_mess[i], uart_mess[i+1])