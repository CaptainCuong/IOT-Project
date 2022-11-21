from ada.utils import client
import random
import time

class ErrorController():
	def __init__(self, init_state):
		assert init_state in [0,1,2,3]
		self.state = init_state
		self.buffer = ''
		self.failures = 0

	def update_state(self):
		if self.state == 0:
			if len(self.buffer) > 0:
				print(f'Change to state 1')
				self.state = 1
		elif self.state == 1:
			print('Change to state 2')
			self.state = 2
		elif self.state == 2:
			if self.failures >= 4:
				print('Change to state 3')
				self.state = 3
			elif not client.receive_ack:
				print('Change to state 1')
				self.state = 1
				self.failures += 1
			elif client.receive_ack:
				print('Change to state 0')
				client.receive_ack = False
				self.state = 0
				self.failures = 0
			else:
				raise
				
		elif self.state == 3:
			raise Exception('Connection Error')
		else:
			pass

	def update_buffer(self):
		rand_num = random.randint(0,10) 
		self.buffer += str(rand_num) if rand_num > 7 else ''

	def reset(self):
		self.state = 0
		self.buffer = ''

	def do_task(self):
		if self.state == 1:
			client.publish('cambien3', random.randint(0,10))
			self.buffer = ''
		elif self.state == 2:
			self.failures += 1

connection = ErrorController(init_state = 0)
counter = 2
client.receive_ack = False
while True:
	connection.update_buffer()
	connection.update_state()
	connection.do_task()
	time.sleep(1)	