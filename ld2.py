
import RPi.GPIO as GPIO
import time




GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.OUT)
while True:
	f=open("/var/www/html/remote/r.txt","r")
	a=f.read()
	if a == "1":
		GPIO.output(3,GPIO.HIGH)
	elif a == "2":
		GPIO.output(3,GPIO.LOW)

	else:
		GPIO.output(3,GPIO.HIGH)


