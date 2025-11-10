import time
import machine

green_led = machine.Pin("GPIO25", machine.Pin.OUT)

while True:
    green_led.value(0)
    time.sleep(0.5)
    green_led.value(1)
    time.sleep(0.5)
