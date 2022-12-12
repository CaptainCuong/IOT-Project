from ..view import *
import sys
import random
import numpy as np
from Adafruit_IO import MQTTClient
import timeit
import time
import random
from ..model.uart_utils import *
from ..model.ai.utils import *

class ViewController(QtCore.QThread):
    signal_light = QtCore.pyqtSignal(str)
    signal_humidity = QtCore.pyqtSignal(str)
    signal_temp = QtCore.pyqtSignal(str)
    signal_ai = QtCore.pyqtSignal(str)
    TIMEOUT = 3
    def __init__(self, parent=None):
        super(ViewController, self).__init__(parent)
        self.is_running = True
        self.buffer = []
        self.state = 0
        self.failures = 0
        
    def run(self):
        COUNTER_AI = 2
        COUNTER_PUBLISH = 2
        COUNTER_SENSOR = 2
        COUNTER_ANHSANG = 5
        COUNTER_UART = 3
        COUNTER_PRESS = 5

        counter_ai = COUNTER_AI
        counter_publish = COUNTER_PUBLISH
        counter_sensor = COUNTER_SENSOR
        counter_anhsang = COUNTER_ANHSANG
        counter_uart = COUNTER_UART
        counter_press = COUNTER_PRESS
        i = 0
        while True:            
            # AI
            if counter_ai == 0:
                state = self.publish_AI()
                self.display_ai(state = state)
                counter_ai = COUNTER_AI

            # Nhiet do,  do am, anh sang
            if counter_anhsang == 0:
                mess = self.publish_light_hum_temp()
                # self.display_light_hum_temp(mess,rand=False)
                counter_anhsang = COUNTER_ANHSANG

            # UART 2 ways
            if counter_uart == 0:
                # publish_uart()
                counter_uart = COUNTER_UART

            self.update_state()

            # Decrease counter
            counter_ai -= 1
            counter_publish -= 1
            counter_anhsang -= 1
            counter_sensor -= 1
            counter_uart -= 1
            counter_press -= 1
            time.sleep(1)

    def display_light_hum_temp(self, mess, rand=False):
        if rand:
            num = str(random.randint(0,100))
            self.signal_humidity.emit(num)
            num = str(random.randint(0,100))
            self.signal_light.emit(num)
            num = str(random.randint(0,100))
            self.signal_temp.emit(num)
        elif len(mess) > 0:
            for m in mess:
                m_lit = str(m[2])
                if m[1] == 'H':
                    self.signal_humidity.emit(m_lit)
                elif m[1] == 'T':
                    self.signal_temp.emit(m_lit)
                elif m[1] == 'L':
                    self.signal_light.emit(m_lit)

    def display_ai(self, state, rand=False):
        if rand:
            num = str(random.randint(0,1))
            self.signal_ai.emit(num)
        else:
            self.signal_ai.emit(str(state))
            if state == 1: # unmasked
                ser.write('1'.encode())
            else:
                ser.write('0'.encode())

    def turn_light_on(self):
        ser.write('3'.encode())

    def turn_light_off(self):
        ser.write('4'.encode())

    def publish(self):
        if len(self.buffer) > 0:
            feed, mess = self.buffer[0]
            client.publish(feed, mess)
            self.buffer = self.buffer[1:]

    def update_state(self):
        if self.state == 0:
            if len(self.buffer) > 0:
                print(f'Change to state 1')
                self.state = 1
        elif self.state == 1:
            print('Change to state 2')
            client.receive_ack = False
            self.timeout = self.TIMEOUT
            self.publish()
            self.state = 2
        elif self.state == 2:
            if self.failures >= 4:
                print('Change to state 3')
                self.state = 3
            elif client.receive_ack:
                print('Change to state 0')
                self.state = 0
                self.failures = 0
            elif not client.receive_ack and self.timeout > 0:
                self.timeout -= 1
            elif not client.receive_ack and self.timeout == 0:
                print('Change to state 1')
                self.state = 1
                self.failures += 1
            else:
                raise   
        elif self.state == 3:
            raise Exception('Connection Error')
        else:
            pass

    def publish_AI(self):
        image_capture()
        new_state = int(image_detector()[0])
        # self.buffer.append(('detect_mask', new_state))
        client.publish('detect_mask',new_state)
        return new_state

    def publish_light_hum_temp(self):
        uart_mess = readSerial()
        if uart_mess:
            print('Update environment:')
            print(uart_mess)
            print('-'*50)
            for mess in uart_mess:
                if mess[1] == 'H':
                    self.buffer.append(('do_am', mess[2]))
                elif mess[1] == 'T':
                    self.buffer.append(('nhiet_do', mess[2]))
                elif mess[1] == 'L':
                    self.buffer.append(('anh_sang', mess[2]))
        return uart_mess

    def connected(self, ada_obj):
        print("Ket noi thanh cong ...")
        [client.subscribe(feed) for feed in AIO_FEED_ID]

    def subscribe(self, ada_obj , userdata , mid , granted_qos):
        print("Subscribe thanh cong ...")

    def disconnected(self, ada_obj):
        print("Ngat ket noi ...")
        sys.exit (1)

    def message(self, ada_obj, feed_id, payload):
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

    def stop(self):
        self.is_running = False
        print('Stopping thread...',self.index)
        self.terminate()

controller = ViewController()

ADAFRUIT_IO_USERNAME = "CaptainCuong"
ADAFRUIT_IO_KEY = "aio_dLAs74WQjKhypHG8YTmpfroyBmIU"
AIO_FEED_ID = ["cambien1", "cambien2", "cambien3", 
               "detect_mask", 'anh_sang', 'nhiet_do', 
               'do_am']

client = MQTTClient(ADAFRUIT_IO_USERNAME , ADAFRUIT_IO_KEY)
client.on_connect = controller.connected
client.on_disconnect = controller.disconnected
client.on_message = controller.message
client.on_subscribe = controller.subscribe
client.connect()
client.loop_background()