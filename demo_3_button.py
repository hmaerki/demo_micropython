import time
import machine

button_red = machine.Pin("GPIO17", machine.Pin.IN, machine.Pin.PULL_UP)
button_white = machine.Pin("GPIO18", machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    print(f"red={button_red.value()} white={button_white.value()}")
    time.sleep(0.1)