import sys
from Adafruit_IO import MQTTClient
import random
import time

AIO_FEED_ID = ["nutnhan1", "nutnhan2","cambien2"]
AIO_USERNAME = "CaptainCuong"
AIO_KEY = "aio_tXuw34H6aXBwGkrmOP57OI8IbO9i"

def connected(self):
    print("Ket noi thanh cong ...")
    for feed_id in AIO_FEED_ID:
        client.subscribe(feed_id)

def subscribe(self , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(self):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Data is from: " + feed_id + ", Payload: " +payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    pass