import tkinter
import serial
import time

ser = serial.Serial(port="COM5",baudrate="115200",timeout=0.1,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,xonxoff=False,rtscts=False,dsrdtr=False)
#
# tkinter.set_appearance_mode("dark")
# tkinter.set_default_color_theme("dark-blue")

app = tkinter.Tk()
app.geometry("900x500")
app.title("HeatingResistor with PID")

def gettingTemperature():
        line = ser.readline().decode().strip()
        line = str(line)
        if ser.isOpen():
                currentTemp_label.configure(text=line)
                currentTemp_label.after(1000, gettingTemperature)

def tempUp():
        data = 'u'
        ser.write(data.encode())

def tempDown():
        data = 'd'
        ser.write(data.encode())


frame = tkinter.Frame(master=app)
frame.pack(pady=20, padx=6, fill="both", expand=True)


#labels
main_label = tkinter.Label(master=frame, text="HeatingResistor with PID", font=("Roboto", 24))
main_label.pack(pady=12, padx=10)


currentTempLab_label = tkinter.Label(master=frame, text="Current Temperature    Reference Temperature", font=("Roboto", 16))
currentTempLab_label.pack(pady=30, padx=15)


currentTemp_label = tkinter.Label(master=frame, font=("Roboto", 16))
currentTemp_label.pack(pady=30, padx=10)

buttonUp = tkinter.Button(master=frame, text="Heat up", command=tempUp, height=3, width=15, fg="red")
buttonUp.pack(pady=12, padx=10)

buttonDown = tkinter.Button(master=frame, text="Heat down", command=tempDown, height=3, width=15, fg='blue')
buttonDown.pack(pady=12, padx=10)


gettingTemperature()

app.mainloop()