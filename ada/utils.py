import numpy as np
from Adafruit_IO import MQTTClient
import timeit
import time
import random
from uart.utils import *
ADAFRUIT_IO_USERNAME = "CaptainCuong"
ADAFRUIT_IO_KEY = "aio_RpZp084IapTzR4DpG0jkvVtOJcMX"
AIO_FEED_ID = ["cambien1", "cambien2", "cambien3", "sent_mess", "detect_mask"]

def connected(self):
    print("Ket noi thanh cong ...")
    client.subscribe('sent_mess')
    client.subscribe('nutnhan1')
    client.subscribe('nutnhan2')
    # [client.subscribe(feed) for feed in AIO_FEED_ID]

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
    if feed_id == 'sent_mess':
        uart_write('sent_mess '+payload)
    if feed_id == 'nutnhan1':
        uart_write('nutnhan1 '+ ('1' if int(payload) == 1 else '2'))
    if feed_id == 'nutnhan2':
        uart_write('nutnhan2 '+ ('3' if int(payload) == 1 else '4'))

def ada_message(feed_id=None, payload=None):
    return feed_id, payload

client = MQTTClient(ADAFRUIT_IO_USERNAME , ADAFRUIT_IO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()