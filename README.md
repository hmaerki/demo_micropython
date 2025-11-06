# demo_micropython

Code snippets to demonstrate Micropython

https://docs.micropython.org/en/latest/rp2/quickref.html#

## Cabling

### OneWire DS18B20

* GND(black): pin33
* DQ(yellow): pin32(GP27)
* 3V3(red): pin36
* DG <-4k7-> 3V3

### Servo

* GND(black): pin3
* SIGNAL(white): pin2(GP1)
* 5V(red): pin40

### red and white button

* GND(black)
* DIP(red): pin22(GP17)
* DIP(white): pin24(GP18)

## Mpy-cross

**Basic bytecode compilation**

`uvx mpy-cross demo_1_onewire.py`

**Native code emission for RP2 (Raspberry Pi Pico)**

`uvx mpy-cross -march=armv6m -X emit=native demo_1_onewire.py`

**All optimizations for maximum performance**

`uvx mpy-cross -march=armv6m -X emit=native -X emit=viper -O3 demo_1_onewire.py`
