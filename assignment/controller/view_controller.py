from model.task.utils import *
from view import *
import sys
import random

class ViewController(QtCore.QThread):
    signal_light = QtCore.pyqtSignal(str)
    signal_humidity = QtCore.pyqtSignal(str)
    signal_temp = QtCore.pyqtSignal(str)
    signal_ai = QtCore.pyqtSignal(str)
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
        COUNTER_ANHSANG = 3
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
                state = publish_AI(self)
                self.display_ai(state = state)
                counter_ai = COUNTER_AI

            # Nhiet do,  do am, anh sang
            if counter_anhsang == 0:
                mess = publish_light_hum_temp(self)
                self.display_light_hum_temp(mess)
                counter_anhsang = COUNTER_ANHSANG

            # UART 2 ways
            if counter_uart == 0:
                # publish_uart()
                counter_uart = COUNTER_UART

            # publish(self)
            update_state(self)

            # Decrease counter
            counter_ai -= 1
            counter_publish -= 1
            counter_anhsang -= 1
            counter_sensor -= 1
            counter_uart -= 1
            counter_press -= 1
            time.sleep(1)

    def display_light_hum_temp(self, mess, random=False):
        if random:
            num = str(random.randint(0,100))
            self.signal_humidity.emit(num)
            num = str(random.randint(0,100))
            self.signal_light.emit(num)
            num = str(random.randint(0,100))
            self.signal_temp.emit(num)
        elif mess:
            for m in mess:
                m_lit = str(m[2])
                if m[1] == 'H':
                    self.signal_humidity.emit(m_lit)
                elif m[1] == 'T':
                    self.signal_temp.emit(m_lit)
                elif m[1] == 'L':
                    self.signal_light.emit(m_lit)

    def display_ai(self, state, random=False):
        if random:
            num = str(random.randint(0,1))
            self.signal_ai.emit(num)
        else:
            self.signal_ai.emit(str(state))
            if state == 1: # unmasked
                ser.write('0'.encode())
            else:
                ser.write('1'.encode())

    def turn_light_on(self):
        ser.write('3'.encode())

    def turn_light_off(self):
        ser.write('4'.encode())

    def stop(self):
        self.is_running = False
        print('Stopping thread...',self.index)
        self.terminate()