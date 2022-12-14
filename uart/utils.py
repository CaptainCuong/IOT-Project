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

def processData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    return splitData

def readSerial():
    bytesToRead = ser.inWaiting()
    ret_mess = []
    if (bytesToRead > 0):
        mess = ser.read(bytesToRead).decode("UTF-8")
        print(mess)
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            ret_mess.append(processData(mess[start:end + 1]))
            mess = mess[end+1:]
            
    return ret_mess

def uart_write(data):
    ser.write((str(data.replace(' ',':')) + "#").encode())

portName = getPort()

if portName != 'None':
    ser = serial.Serial(port=portName, baudrate=115200)
else:
    raise Exception('Port None')