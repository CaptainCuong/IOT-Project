from uart.utils import *

STATE = ['0','1','3','4']
i=0
while True:
    signals = readSerial()
    if signals:
        for signal in signals:
            print(signal)
    ser.write(STATE[i].encode())
    i = (i+1)%len(STATE)
    print(i)
    time.sleep(3)