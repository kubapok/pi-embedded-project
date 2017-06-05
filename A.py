import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


x = [19,13,5,6,22,27,4,17] # lewa strona
y = [18,23,24,25,12,16,20,21] # prawa strona

sleep_time = 0.001




def empty():
	for x_0 in x:
		for y_0 in y:
			GPIO.setup(y_0,GPIO.OUT)
			GPIO.setup(x_0,GPIO.OUT)

			GPIO.output(x_0,GPIO.HIGH)
			GPIO.output(y_0,GPIO.LOW)


def light(points):
	try:
		while True:
			for point in points:
				GPIO.output(point[0],GPIO.LOW)
				GPIO.output(point[1],GPIO.HIGH)
				time.sleep(sleep_time)
				GPIO.output(point[0],GPIO.HIGH)
				GPIO.output(point[1],GPIO.LOW)
	except KeyboardInterrupt:
		print 'ending'
		empty()


A_points = [
	[x[0],y[7]],
	[x[1],y[6]],
	[x[2],y[5]],
	[x[3],y[4]],
	[x[4],y[5]],
	[x[5],y[6]],
	[x[6],y[7]],
	[x[2],y[6]],
	# teraz bedzie kreseczka
	[x[2],y[6]],
	[x[3],y[6]],
	[x[4],y[6]],
]

empty()
light(A_points)
