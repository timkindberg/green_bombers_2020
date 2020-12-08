from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
import math

hub = PrimeHub()

# Slide Challenge - Alex
motor_pair = MotorPair('E','F')
motor_pair.set_motor_rotation(8.71 * math.pi,'cm')
motor_pair.move(3,unit='in',steering=0,speed=5) #forward
motor_pair.move(20,unit='in',steering=0,speed=25) #forward
motor_pair.move(5,unit='in',steering=0,speed=-10) #backward
motor_pair.move(25,unit='in',steering=-5,speed=-50) #backward

###########   
###########
