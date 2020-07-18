import serial
import time
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

ser = serial.Serial('COM5', baudrate = 9600, timeout = 1)
time.sleep(3)

arrayVout = np.zeros(5).reshape(5)

while(1):
    print("-------------------------------------------------")
    print("Started at " + datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    
    ser.write(b'g')
    arduinoData = ser.readline().decode().split(' ')

    arrayVout[0] = float(arduinoData[0]) * 5 / 1023
#    arrayVout[1] = float(arduinoData[1]) * 5 / 1023
#    arrayVout[2] = float(arduinoData[2]) * 5 / 1023
#    arrayVout[3] = float(arduinoData[3]) * 5 / 1023
#    arrayVout[4] = float(arduinoData[4]) * 5 / 1023

    print(arrayVout)
    print("Finished at " + datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    time.sleep(0.1) # seconds

