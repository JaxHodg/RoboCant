from gpiozero import Servo
from time import sleep

servo = Servo(17) #gpio pin

try:
	while True:
		servo.min()
		sleep(0.5)
		servo.mid()
		sleep(0.5)
		servo.max()
		sleep(5)
except KeyboardInterrupt:
	Print("lmao")
