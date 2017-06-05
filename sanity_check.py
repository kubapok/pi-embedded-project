import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


x = [17,4,27,22,6,5,13,19] # lewa strona
y = [18,23,24,25,12,16,20,21] # prawa strona

sleep_time = 0.1

for x_0 in x:
	for y_0 in y:
		GPIO.setup(y_0,GPIO.OUT)
		GPIO.setup(x_0,GPIO.OUT)

		GPIO.output(x_0,GPIO.HIGH)
		GPIO.output(y_0,GPIO.LOW)


for x_0 in x:
	for y_0 in y:
		GPIO.setup(y_0,GPIO.OUT)
		GPIO.setup(x_0,GPIO.OUT)



		print "LED on"
		GPIO.output(x_0,GPIO.LOW)
		GPIO.output(y_0,GPIO.HIGH)
		time.sleep(sleep_time)
		print "LED off"
		GPIO.output(x_0,GPIO.HIGH)
		GPIO.output(y_0,GPIO.LOW)
