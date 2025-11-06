import machine

min_duty = 1802
max_duty = 7864

pwm_frequency = 50
servo = machine.PWM(machine.Pin(1))
servo.freq(pwm_frequency)

green_led = machine.PWM(machine.Pin(25), duty_u16=2**15)
green_led.freq(8)

class Button:
    def __init__(self, gpio: int, duty: int):

        def handler(pin):
            servo.duty_u16(duty)

        pin = machine.Pin(gpio, machine.Pin.IN, machine.Pin.PULL_UP)
        pin.irq(handler, hard=True) 

button_red = Button(17, min_duty)
button_white = Button(18, max_duty)

