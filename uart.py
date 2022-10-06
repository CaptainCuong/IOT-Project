print('Hello Sensors')
import serial.tools.list_ports
import time

def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB-SERIAL" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    return commPort

mess = ""
def processData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    
def readSerial():
    bytesToRead = ser.inWaiting()
    print(bytesToRead)
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start:end + 1])
            if (end == len(mess)):
                print('Here1')
                mess = ""
            else:
                print('Here2')
                mess = mess[end+1:]

portName = getPort()

if portName != 'None':
    ser = serial.Serial(port=portName, baudrate=115200)
else:
    raise Exception('Port None')

while True:
    print(ser)
    readSerial()
    time.sleep(1)