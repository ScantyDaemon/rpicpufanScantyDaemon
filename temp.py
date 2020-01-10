import  RPi.GPIO as GPIO
import time
import subprocess
import os
import datetime
GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
def cpufan():
	tFile = open('/sys/class/thermal/thermal_zone0/temp')
	temp = float(tFile.read())
	tempC = temp/1000
	if tempC > 43:
		GPIO.setup(2, GPIO.OUT)
		GPIO.setup(2,GPIO.HIGH)
		#print('hot')
	else:
		GPIO.setup(2, GPIO.OUT)
		GPIO.output(2,GPIO.LOW)
		#print('cold')
def button():
	GPIO.setup(18, GPIO.IN,pull_up_down=GPIO.PUD_UP)
	inputValue = GPIO.input(18)
	if (inputValue == False):
		subprocess.run(["poweroff"])

while True:
	cpufan()
	button()
	time.sleep(0.1)
