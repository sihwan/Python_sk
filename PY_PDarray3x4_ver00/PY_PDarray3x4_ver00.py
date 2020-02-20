import serial
import time
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

ser = serial.Serial('COM25', baudrate = 9600, timeout = 1)
time.sleep(3)

GrayBarOn = "y"
nrows, ncols = 3, 4
arrayVout = np.zeros(nrows * ncols).reshape((nrows, ncols))

while(1):
#for j in range(1,3):
    print("-------------------------------------------------")
    print("Started at " + datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    
    ser.write(b'g')
    arduinoData = ser.readline().decode().split(' ')

    arrayVout[0,0] = float(arduinoData[0])
    arrayVout[1,0] = float(arduinoData[1])
    arrayVout[2,0] = float(arduinoData[2])
    arrayVout[0,1] = float(arduinoData[3])
    arrayVout[1,1] = float(arduinoData[4])
    arrayVout[2,1] = float(arduinoData[5])
    arrayVout[0,2] = float(arduinoData[6])
    arrayVout[1,2] = float(arduinoData[7])
    arrayVout[2,2] = float(arduinoData[8])
    arrayVout[0,3] = float(arduinoData[9])
    arrayVout[1,3] = float(arduinoData[10])
    arrayVout[2,3] = float(arduinoData[11])

    print(arrayVout)
    print("Finished at " + datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

    if GrayBarOn == "y":
        plt.imshow(arrayVout, cmap='gray', vmin=0, vmax=5)
        plt.colorbar()
        plt.show()

