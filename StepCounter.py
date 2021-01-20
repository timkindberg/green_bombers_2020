from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
import math

hub = PrimeHub()
motor_pair = MotorPair('E','F')
motor_pair.set_motor_rotation(8.71 * math.pi,'cm')

def turn(stop_angle, speed=10):
    hub.motion_sensor.reset_yaw_angle()
    motor_pair.start(speed=speed, steering=100 if stop_angle > 0 else -100)
    start_angle = current_angle = hub.motion_sensor.get_yaw_angle() + 180
    while(current_angle < stop_angle + 180 if stop_angle > 0 else current_angle > stop_angle + 180):
        current_angle = hub.motion_sensor.get_yaw_angle() + 180
        print("current angle: {}".format(current_angle))
    motor_pair.stop()

def boogie():
    while(True):
        hub.speaker.set_volume(100)
        hub.speaker.beep(note=60, seconds=0.2)
        hub.speaker.beep(note=80, seconds=0.2)
        hub.speaker.beep(note=100, seconds=0.2)
        hub.speaker.beep(note=120, seconds=0.2)
        motor_pair.move(1, unit='in', speed=50)
        motor_pair.move(1, unit='in', speed=-50)
        motor_pair.move(1, unit='in', speed=50)
        motor_pair.move(1, unit='in', speed=-50)
        hub.speaker.start_beep(note=90)
        turn(160, speed=25)
        hub.speaker.stop()
        turn(-30, speed=25)
        turn(30, speed=25)
        turn(-30, speed=25)
        turn(30, speed=25)
        turn(-3, speed=60)
        turn(3, speed=60)
        turn(-3, speed=60)
        turn(3, speed=60)
        turn(-3, speed=60)
        turn(3, speed=60)





#Zander Mission slot 3
motor_pair.move_tank(45, unit='in', left_speed=-67, right_speed=-70) #30 no attachment

motor_pair.move(1.5, unit='in', speed=20)
turn(-90)
motor_pair.move(1, unit='in', speed=20)
motor_pair.move(22, unit='in', speed=-50)
turn(-29)
motor_pair.move(16.5, unit='in', speed=-50)

boogie()
