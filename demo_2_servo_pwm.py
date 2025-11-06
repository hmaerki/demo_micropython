import machine
import time

min_duty = 1802
max_duty = 7864

pwm_frequency = 50
servo = machine.PWM(machine.Pin(1))
servo.freq(pwm_frequency)

def set_servo(angle: float):
    duty = (max_duty-min_duty) * (angle/180) + min_duty
    servo.duty_u16(int(duty))

while True:
    for angle in (45.0, 60.0, 90.0, 120.0, 90.0, 60.0):
        set_servo(angle)
        time.sleep(1) 