import time
import serial

serial_port = serial.Serial(port="COM5",
                                    baudrate="115200",
                                    timeout=0.1,
                                    bytesize=serial.EIGHTBITS,
                                    parity=serial.PARITY_NONE,
                                    stopbits=serial.STOPBITS_ONE,
                                    xonxoff=False,
                                    rtscts=False,
                                    dsrdtr=False)


data = 60
serial_port.write(data)
time.sleep(0.5)

