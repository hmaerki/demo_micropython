import time
import machine

DEBOUNCE = False

BOUNCE_TIME_US = 1_000_000

green_led = machine.PWM(machine.Pin(25), duty_u16=2**15)
green_led.freq(8)

class Button:
    def __init__(self, gpio: int, color: str):
        self.ticks_pressed_us = 0

        def handler(pin: machine.Pin):
            if DEBOUNCE:
                if time.ticks_diff(time.ticks_us(), self.ticks_pressed_us) > BOUNCE_TIME_US:
                    self.ticks_pressed_us = time.ticks_us()
                    if pin.value() == 0:
                        print(color)
            else:
                print(color, pin.value())

        pin = machine.Pin(gpio, machine.Pin.IN, machine.Pin.PULL_UP)
        pin.irq(handler, hard=True)  

button_red = Button("GPIO17", "red")
button_white = Button("GPIO18", "white")

while True:
    print("...")
    time.sleep(1)
