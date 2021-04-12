
import serial
from time import sleep


ser = serial.Serial("/dev/ttyS0",baudrate=115200)
y = 4
x = b'\x02'
ser.write(x)