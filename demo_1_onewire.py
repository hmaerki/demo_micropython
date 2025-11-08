import time
import machine
import onewire
import ds18x20

ow = onewire.OneWire(machine.Pin("GPIO27"))
ds = ds18x20.DS18X20(ow)
serials = ds.scan()
while True:
    ds.convert_temp()
    time.sleep_ms(750)
    for serial in serials:
        print(f"{ds.read_temp(serial):0.1f}C {serial}")
    time.sleep_ms(2000)
