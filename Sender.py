from tkinter import *
from tkinter import messagebox
import serial

ser = serial.Serial(
    port = '/dev/ttyAMA0',
    baudrate = 9600,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1)

def init(win):
    win.title("Hello")
    win.minsize(500, 200)
    comp.pack()
    
def sendA():	//send 'A' via uart
    try:
        ser.write(str.encode('A'))
        ser.flush()
    except KeyboardInterrupt:
        ser.close()
    
def sendB():	//send 'B' via uart
    try:
        ser.write(str.encode('B'))
        ser.flush()
    except KeyboardInterrupt:
        ser.close()
    
def sendC():	//send 'C' via uart
    try:
        ser.write(str.encode('C'))
        ser.flush()
    except KeyboardInterrupt:
        ser.close()
    
win = Tk()
positionRight = 300
positionDown = 300

win.geometry("+{}+{}".format(positionRight, positionDown))

comp = Button(win, text="Send A", command=sendA)
comp.pack()
comp = Button(win, text="Send B", command=sendB)
comp.pack()
comp = Button(win, text="Send C", command=sendC)
comp.pack()

init(win)
mainloop()