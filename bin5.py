import RPi.GPIO as GPIO 

import signal
import time

 
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

TRIG = 23 
ECHO = 24 
LED = 25


#....bin2 

print("Bin3-Waste Measurement In Progress")
GPIO.setup(TRIG,GPIO.OUT) 
GPIO.setup(ECHO,GPIO.IN)
while True : 
	
	GPIO.output(TRIG, False) 
	print("Waiting For Sensor To Settle") 
	time.sleep(2) 
	GPIO.output(TRIG, True) 
	time.sleep(0.00001) 
	GPIO.output(TRIG, False) 
	while GPIO.input(ECHO)==0:
  		pulse_start = time.time() 
	while GPIO.input(ECHO)==1:
  		pulse_end = time.time() 
	pulse_duration = pulse_end - pulse_start 
	level = pulse_duration * 17150
	#print(level) 
	level = (100 -( (level / 28 )* 100)) 
	level = round(level) 
	print "Current level : ",level,"%"
	time.sleep(2) 
GPIO.cleanup()
