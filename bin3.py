import RPi.GPIO as GPIO 

import signal
import time

import requests
from requests.exceptions import ConnectionError
 
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

TRIG = 23 
ECHO = 24 
LED = 25
api="6JXO9Z1XQOPI3RC7"
def sender(trash_no,level):

       if trash_no == 3:
		
                payload = {'key': api, 'field1' : str(level)}
       try :
       		r = requests.post("https://api.thingspeak.com/update.json",params=payload)
      	#	print r.text
                print "Updated to thingspeak channel"
       except ConnectionError as e:   
   		print

#....bin2 
def sender2(bin_no,level):

     url = 'http://smartbin.esy.es/waste_bin_script.php'
     data = dict(bin_no=bin_no, waste_amt=level)

     r = requests.post(url, data=data, allow_redirects=True)
     print r.content
     print "Updated to database"
print("Bin3-Waste Measurement In Progress")
GPIO.setup(TRIG,GPIO.OUT) 
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)
GPIO.output(LED, False)
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
	level = (100 -( (level / 32 )* 100)) 
	level = round(level)
	if level < 2 :
		level = 0
	if level > 70 :
		GPIO.output(LED, True)
	else:
		GPIO.output(LED, False)
 
	print "Current level : ",level,"%"
	sender(3,level)
        sender2(3,level );
	time.sleep(2) 
GPIO.cleanup()
