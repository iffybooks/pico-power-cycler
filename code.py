# Pico Power Cycler Kit
# 2025 Iffy Books (wtfpl)
# https://iffybooks.net/pico-power-cycler

import board
import digitalio
import time

# Initialize MOSFET pin
mosfet_pin = digitalio.DigitalInOut(board.GP8)
mosfet_pin.direction = digitalio.Direction.OUTPUT

# Infinite loop
while True:
	# Turn power on
	mosfet_pin.value = True
	time.sleep(3)
	# Turn power off
	mosfet_pin.value = False
	time.sleep(3)
