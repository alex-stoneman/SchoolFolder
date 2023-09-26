from __future__ import division
from time import sleep

try:
    from gpiozero import CamJamKitRobot
    print("GPIO Zero found")

    robot = CamJamKitRobot()
    motor_left = robot.left_motor
    motor_right = robot.right_motor
    motor_multiplier = -1

    def set_speeds(power_left, power_right):
        power_left = (motor_multiplier * power_left) / 100
        power_right = (motor_multiplier * power_right) / 100

        if power_left < 0:
            motor_left.backward(-power_left)
        else:
            motor_left.forward(power_left)

        if power_right < 0:
            motor_right.backward(-power_right)
        else:
            motor_right.forward(power_right)


    def stop_motors():
        motor_left.stop()
        motor_right.stop()


except ImportError:
    def set_speeds(power_left, power_right):
        print("Debug Left: {}, Right: {}", format(power_left, power_right))
        sleep(0.3)


    def stop_motors():
        print("Debug Motors Stopping")


from approxeng.input.selectbinder import ControllerResource

class RobotStopException(Exception):
    pass

def mixer(yaw, throttle, max_power=100):
    left = throttle + yaw
    right = throttle - yaw
    scale = float(max_power) / max(1, abs(left), abs(right))
    return int(left * scale), int(right * scale)


try:
    while True:
        try:
            with ControllerResource(dead_zone=0.1, hot_zone=0.2) as joystick:
                print("Controller found - press home to exit ")
                print(joystick.controls)
                while joystick.connected:
                    x_axis, y_axis = joystick["lx", "ly"]
                    power_left, power_right = mixer(yaw=x_axis, throttle=y_axis)
                    set_speeds(power_left, power_right)
                    joystick.check_presses()
                    if joystick.has_presses:
                        print(joystick.presses)
                    if "home" in joystick.presses:
                        raise RobotStopException()
        except IOError:
            print("No Controller found yet")
            sleep(1)
except RobotStopException:
    stop_motors()

