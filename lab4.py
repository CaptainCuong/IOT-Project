from uart.utils import *
from ada.utils import *

while True:
	uart_mess = readSerial()
	if uart_mess:
		print('Message from UART:')
		print(uart_mess)
		print('-'*50)
		for i in range(0, len(uart_mess), 2):
			if uart_mess[i] in ['cambien1','cambien2','cambien3']:
				client.publish(uart_mess[i], uart_mess[i+1])

	