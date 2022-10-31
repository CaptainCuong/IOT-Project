import numpy as np
from Adafruit_IO import MQTTClient
import timeit
import time
import random
from uart.utils import *
ADAFRUIT_IO_USERNAME = "CaptainCuong"
ADAFRUIT_IO_KEY = "aio_tXuw34H6aXBwGkrmOP57OI8IbO9i"
AIO_FEED_ID = ["cambien1", "cambien2", "cambien3"]
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

def message(self, feed_id, payload):
    if payload:
        print("Data is from: " + feed_id + ", Payload: " + payload)
    if feed_id == 'cambien1':
        uart_write('cambien1 '+payload)
    if feed_id == 'cambien2':
        uart_write('cambien2 '+payload)
    if feed_id == 'cambien3':
        uart_write('cambien3 '+payload)

def ada_message(feed_id=None, payload=None):
    return feed_id, payload

client = MQTTClient(ADAFRUIT_IO_USERNAME , ADAFRUIT_IO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()