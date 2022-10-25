from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import cv2
from Adafruit_IO import MQTTClient
import timeit
import time
import random

ADAFRUIT_IO_USERNAME = "CaptainCuong"
ADAFRUIT_IO_KEY = "aio_tXuw34H6aXBwGkrmOP57OI8IbO9i"
AIO_FEED_ID = ["nutnhan1", "nutnhan2"]
SENSORS = ['cambien1','cambien2','cambien3']

def connected(self):
    print("Ket noi thanh cong ...")
    client.subscribe('detect_mask')
    [client.subscribe(feed) for feed in AIO_FEED_ID]

def subscribe(self , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(self):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
	if payload == 'nutnhan1_on':
		print('Nut nhan 1: ON')
	elif payload == 'nutnhan1_off':
		print('Nut nhan 1: OFF')
	elif payload == 'nutnhan2_on':
		print('Nut nhan 2: ON')
	elif payload == 'nutnhan2_off':
		print('Nut nhan 2: OFF')
	else:
		print('Not recognized')
    # print("Data is from: " + feed_id + ", Payload: " + payload)

client = MQTTClient(ADAFRUIT_IO_USERNAME , ADAFRUIT_IO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()


# Load the model
model = load_model('keras_model.h5')



cam = cv2.VideoCapture(0)
def image_capture():
	ret, frame = cam.read()
	cv2.imwrite("input.png", frame)

def image_detector():
	# Create the array of the right shape to feed into the keras model
	# The 'length' or number of images you can put into the array is
	# determined by the first position in the shape tuple, in this case 1.
	data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
	# Replace this with the path to your image
	image = Image.open('input.png').convert('RGB')
	#resize the image to a 224x224 with the same strategy as in TM2:
	#resizing the image to be at least 224x224 and then cropping from the center
	size = (224, 224)
	image = ImageOps.fit(image, size, Image.ANTIALIAS)

	#turn the image into a numpy array
	image_array = np.asarray(image)
	# Normalize the image
	normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
	# Load the image into the array
	data[0] = normalized_image_array

	# run the inference
	prediction = model.predict(data)
	state = np.argmax(prediction,axis=1)
	return state

# def wait_5s():
# 	a = 0
# 	start = timeit.default_timer()
# 	for i in range(120000000):
# 		a+=1
# 	stop = timeit.default_timer()
# 	print(str(stop-start)+ ' elapsed')

if __name__ == '__main__':
	client.loop_background()
	counter_ai = 3
	counter_publish = 2
	i = 0
	while True:
		i = (i+1)%3

		if counter_publish == 0: 
			client.publish(f'cambien{i+1}', random.randint(0,10))
			counter_publish = 5

		if counter_ai == 0:
			image_capture()
			new_state = int(image_detector()[0])
			client.publish('detect_mask', new_state)
			counter_ai = 5

		counter_ai -= 1
		counter_publish -= 1
		time.sleep(1)
		
		
	
		
	# state = 0 # no_mask
	# while True:
	# 	image_capture()
	# 	new_state = int(image_detector()[0])
	# 	print(type(new_state))
	# 	if new_state != state:
	# 		state = new_state
	# 		print('Change state, need to publish')
	# 		client.publish('detect_mask', new_state)