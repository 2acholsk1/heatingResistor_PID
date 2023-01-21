import serial
import time
import signal
import matplotlib.pyplot as plt

ser = serial.Serial("COM3", 115200, parity=serial.PARITY_NONE)

with open("data.csv", "w", newline="") as file:
    while True:
        line = ser.readline().decode().strip()
        print(line)
        file.write(line + ',')
        time.sleep(0.01)