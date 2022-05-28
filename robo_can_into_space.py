from gpiozero import DistanceSensor, Servo, Device
from gpiozero.pins.pigpio import PiGPIOFactory
import sys, select

from time import sleep

Device.pin_factory = PiGPIOFactory()

servo = Servo(17)
ultrasonic = DistanceSensor(echo=24,trigger=18)

nfc_id = ""

servo.max()

def in_range(): # Detects object on can
	print("Detected Object ", ultrasonic.distance)
	sleep(5)
	if (nfc_id == ""): # If no nfc_id saved then must be garbage
		servo.min()
		print("Dumped Garbage")
		sleep(5)
		servo.max()
	else: #If nfc_id saved then refund
		servo.min()
		print("Dumped NFC Tag ", nfc_id)
		sleep(5)
		servo.max()

ultrasonic.when_in_range = in_range

while (True): # Sets nfc_id when NFC tag is read, erases after 10 seconds
	nfc_id = input()
	print("Read NFC Tag ", nfc_id)
	sleep(10)
	nfc_id = ""

