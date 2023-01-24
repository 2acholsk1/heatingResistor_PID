import serial
import time
import signal


ser = serial.Serial("COM5", 115200, parity=serial.PARITY_NONE)

with open("data.csv", "w", newline="") as file:
    while True:
        line = ser.readline().decode().strip()
        print(line)
        file.write(line + ',')
        time.sleep(0.01)

    