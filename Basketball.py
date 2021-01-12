from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
import math

hub = PrimeHub()
hub.motion_sensor.reset_yaw_angle()
motor_pair = MotorPair( 'E','F' )
motor_pair.set_motor_rotation(8.71 * math.pi,'cm')
raiser = Motor('A')

def turn(stop_angle, speed=7):
    hub.motion_sensor.reset_yaw_angle()
    motor_pair.start(speed=speed, steering=100 if stop_angle > 0 else -100)
    start_angle = current_angle = hub.motion_sensor.get_yaw_angle() + 180
    while(current_angle < stop_angle + 180 if stop_angle > 0 else current_angle > stop_angle + 180):
        current_angle = hub.motion_sensor.get_yaw_angle() + 180
        print("current angle: {}".format(current_angle))
    motor_pair.stop()   



motor_pair.move(5,unit='in',steering=0,speed=-10)
motor_pair.move(25,unit='in',steering=0,speed=-30)
turn(-80)
motor_pair.move(8,unit='in',steering=0,speed=-30)
motor_pair.move(3,unit='in',steering=0,speed=-10)
raiser.run_for_degrees(-1229, 80)
motor_pair.move(3,unit='in',steering=0,speed=10)
motor_pair.move(8,unit='in',steering=0,speed=30)
turn(80)
motor_pair.move(30,unit='in',steering=0,speed=50)
