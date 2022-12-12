import numpy as np
from Adafruit_IO import MQTTClient
import timeit
import time
import random
from .uart_utils import *
from ..controller.view_controller import controller

ADAFRUIT_IO_USERNAME = "CaptainCuong"
ADAFRUIT_IO_KEY = "aio_dLAs74WQjKhypHG8YTmpfroyBmIU"
AIO_FEED_ID = ["cambien1", "cambien2", "cambien3", 
               "detect_mask", 'anh_sang', 'nhiet_do', 
               'do_am']

def connected(ada_obj):
    print("Ket noi thanh cong ...")
    [client.subscribe(feed) for feed in AIO_FEED_ID]

def subscribe(ada_obj , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(ada_obj):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(ada_obj, feed_id, payload):
    ada_obj.receive_ack = True
    if payload:
        print("Data is from: " + feed_id + ", Payload: " + payload)
    if feed_id == 'anh_sang':
        controller.signal_light.emit(str(payload))
    if feed_id == 'nhiet_do':
        controller.signal_temp.emit(str(payload))
    if feed_id == 'do_am':
        controller.signal_humidity.emit(str(payload))
    if feed_id == 'detect_mask':
        pass


# def ada_message(feed_id=None, payload=None):
#     return feed_id, payload

client = MQTTClient(ADAFRUIT_IO_USERNAME , ADAFRUIT_IO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()