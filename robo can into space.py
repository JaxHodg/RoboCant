from gpiozero import DistanceSensor
from gpiozero import Servo
from time import sleep

servo = Servo(17)
ultrasonic = DistanceSensor(echo=24, trigger=18, threshold_distance=0.35)


def in_range():
    servo.min()
    sleep(5)
    servo.max()


ultrasonic.when_in_range = in_range
