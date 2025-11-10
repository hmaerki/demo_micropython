import machine

green_led = machine.PWM(machine.Pin("GPIO25"), duty_u16=2**15)
green_led.freq(8)