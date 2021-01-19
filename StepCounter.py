from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

hub = PrimeHub() 
import math
#Zander Mission slot 3 
motor_pair = MotorPair('E','F')
motor_pair.move_tank(33, unit='in', left_speed=-97, right_speed=-100) #30 no attachment
motor_pair.move_tank(30, unit='in', left_speed=100, right_speed=99) 

