from gpiozero import DistanceSensor, Servo, Device
from gpiozero.pins.pigpio import PiGPIOFactory

from time import sleep

Device.pin_factory = PiGPIOFactory()

servo = Servo(17)
ultrasonic = DistanceSensor(echo=24, trigger=18, threshold_distance=0.35)


def in_range():
    servo.min()
    sleep(5)
    servo.max()


ultrasonic.when_in_range = in_range

while True:
    input()
