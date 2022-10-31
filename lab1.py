import time
import random
from Adafruit_IO import MQTTClient

AIO_FEED_ID = ["nutnhan1", "nutnhan2"]
SENSORS = ['cambien1','cambien2','cambien3']
ADAFRUIT_IO_USERNAME = "CaptainCuong"
ADAFRUIT_IO_KEY = "aio_tXuw34H6aXBwGkrmOP57OI8IbO9i"

def connected(self):
    print("Ket noi thanh cong ...")
    [client.subscribe(feed) for feed in AIO_FEED_ID]

def subscribe(self , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(self):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(self, feed_id , payload):
    print("Data is from: " + feed_id + ", Payload: " +payload)

client = MQTTClient(ADAFRUIT_IO_USERNAME , ADAFRUIT_IO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()


rand_sensors = random.choices(SENSORS, k=3)

while True:
	# client.subscribe(rand_sensors[0], random.randint(0,10))
	# for i in range(100000): i+=1
	# client.subscribe(rand_sensors[1], random.randint(0,10))
	# for i in range(100000): i+=1
	# client.subscribe(rand_sensors[2], random.randint(0,10))
	# for i in range(100000): i+=1
	# time.sleep(1)
    time.