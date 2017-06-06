from __future__ import print_function
import RPi.GPIO as GPIO
import time
import re
import sys
import os
import getopt
from lazyme.string import color_print


os.system('clear')
sys.stdout.flush()

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


def light(points, letter_time):
	a = time.time()
	while time.time() - a < letter_time:
		for point in points:
			GPIO.output(point[0],GPIO.LOW)
			GPIO.output(point[1],GPIO.HIGH)
			time.sleep(sleep_time)
			GPIO.output(point[0],GPIO.HIGH)
			GPIO.output(point[1],GPIO.LOW)


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

B_points = [
	[x[0],y[7]],
	[x[0],y[6]],
	[x[0],y[5]],
	[x[0],y[4]],
	[x[0],y[3]],
	[x[0],y[2]],
	[x[1],y[2]],
	[x[2],y[2]],
	[x[3],y[6]],
	[x[3],y[5]],
	[x[3],y[4]],
	[x[3],y[3]],
	[x[1],y[4]],
	[x[2],y[4]],
	[x[1],y[7]],
	[x[2],y[7]],
]




C_points = [
	[x[0],y[7]],
	[x[0],y[6]],
	[x[0],y[5]],
	[x[0],y[4]],
	[x[0],y[3]],
	[x[0],y[2]],
	[x[1],y[2]],
	[x[2],y[2]],
	[x[3],y[2]],
	[x[1],y[7]],
	[x[2],y[7]],
	[x[3],y[7]],
]


letter_dict = {'A':A_points,
		'B':B_points,
		'C':C_points,
		}



def is_letters_valid(letters):
	return re.search('^[abcABC]*$', letters)	

def is_letters_duration_time_valid(d_time):
	return re.search('^\d$', d_time) 


optlist, args = getopt.getopt(sys.argv[1:], ':t:s:')
for i in optlist:
	if i[0] == '-t':
		letter_time = i[1]
	if i[0] == '-s':
		letters = i[1]

empty()
# letters = 'abcabc' # USER DEFINED
# letter_time = '1' # USER DEFINED




try:
	if not is_letters_valid(letters):
		sys.exit(1)
	letters = letters.upper()
except:
	print('given string should contain only A, B and C')
	sys.exit(1)
	
try:
	if not is_letters_duration_time_valid(letter_time):
		sys.exit(1)
	letter_time = int(letter_time)
except:
	print('given time should be integer > 0 and < 10')
	sys.exit(1)

try:
	for i in range(len(letters)):
		sys.stdout.flush()
		os.system('clear')
		print(letters[:i],end='')
		color_print( letters[i], color = 'red', end='')
		print(letters[i+1:])
		light(letter_dict[letters[i]], letter_time)
		sys.stdout.flush()
except KeyboardInterrupt:
	print
	print('bye')
	empty()
	sys.exit(1)
	

print('bye')
