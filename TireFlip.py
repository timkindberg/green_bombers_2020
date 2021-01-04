from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
import math

hub = PrimeHub()
hub.motion_sensor.reset_yaw_angle()

def turn(stop_angle, speed=7):
    hub.motion_sensor.reset_yaw_angle()
    motor_pair.start(speed=speed, steering=100 if stop_angle > 0 else -100)
    start_angle = current_angle = hub.motion_sensor.get_yaw_angle() + 180
    while(current_angle < stop_angle + 180 if stop_angle > 0 else current_angle > stop_angle + 180):
        current_angle = hub.motion_sensor.get_yaw_angle() + 180
        print("current angle: {}".format(current_angle))
    motor_pair.stop()

def flip_tire(move_back_distance):
    flipper.start_at_power(50)
    wait_for_seconds(1.5)
    motor_pair.move(move_back_distance,unit='in',steering=0,speed=-50)
    flipper.stop()


# Tire Flip - Sam - 14
motor_pair = MotorPair('E','F')
motor_pair.set_motor_rotation(8.75 * math.pi,'cm')
flipper = Motor('D')
flipper.set_stall_detection(False)
flipper.set_degrees_counted(0)

#1
# motor_pair.move(7,unit='in',steering=0,speed=8)
# motor_pair.move(48,unit='in',steering=0,speed=58)
# turn(-130)
# motor_pair.move(2.85,unit='in',steering=0,speed=8)
# flip_tire(8)
# motor_pair.move(8,unit='in',steering=0,speed=25) # push tire forward

#2
motor_pair.move(7,unit='in',steering=0,speed=8)
motor_pair.move(46,unit='in',steering=0,speed=58)
turn(-90)
motor_pair.move(8,unit='in',steering=0,speed=-15)
motor_pair.move(7.75,unit='in',steering=0,speed=25) # push tire forward
turn(-35)
flip_tire(8)
motor_pair.move(8,unit='in',steering=0,speed=25) # push tire forward






