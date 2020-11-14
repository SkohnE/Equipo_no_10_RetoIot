import serial

ser = serial.Serial("/dev/cu.usbmodem14101", 9600);
while(1):
    print(ser.readline())