import RPi.GPIO as GPIO
import time
from sense_hat import SenseHat
import serial

ser = serial.Serial(
port='/dev/ttyUSB0',
baudrate = 9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1)


sense = SenseHat()

#GPIO - actuators
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

deadzone = 2 #meters

#from last year
def get_height():
    return ((((1013.25 / get_Pressure()) ** (1 / 5.257)) - 1) * (get_Temperature() + 273.15)) / 0.0065
## Functions
def openValve():
	#open inflation-valve
    	print("open inflation-valve")
	#close deflation-valve
    	print("close deflation-valve")
    
def closeValve():
    	#close inflation-valve
    	print("close inflation-valve")
	#open deflation-valve
   	print("open deflation-valve")
def close():
     	#close inflation-valve
    	print("close inflation-valve")
	#close deflation-valve
    	print("close deflation-valve")
    
def onOff(ref, sensor, deadzone):
    	if sensor < (ref - deadzone):
        	openValve()
        
    	elif sensor > (ref + deadzone):
        	closeValve()
    	else:
        	close()

while(True):
	ref = ser.readline()
	altitude = get_height()

	onOff(ref, sensor, deadzone)
		