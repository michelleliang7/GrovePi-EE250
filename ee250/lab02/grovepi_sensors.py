""" EE 250L Lab 02: GrovePi Sensors

List team members here.

Insert Github repository link here.
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time


# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
from grove_rgb_lcd import *


"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
    PORT = 4    # D4
    full_angle = 300
	adc_ref = 5
	grove_vcc = 5
	potentiometer = 0
	sensor_old = -1
	dist_old = -1
	dist = sensor_value = -1
	grovepi.pinMode(potentiometer,"INPUT")
    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)

        #print(grovepi.ultrasonicRead(PORT))
		# Read distance value from Ultrasonic
    	try:
        # Read distance value from Ultrasonic
        	dist = grovepi.ultrasonicRead(ultrasonic_ranger)
		except TypeError:
			print ("Error")
		except IOError:
			print ("Error")

		# Read sensor value from potentiometer
		try:
			sensor_value = grovepi.analogRead(potentiometer)
		except KeyboardInterrupt:
			break
		except IOError:
			print ("Error")

		# Calculate voltage
		voltage = round((float)(sensor_value) * adc_ref / 1023, 2)

		# Calculate rotation in degrees (0 to 300)
		degrees = round((voltage * full_angle) / grove_vcc, 2)

		# Calculate threshold distance determined by potentiometer
		thresh = 517/300*degrees

		if sensor_value != sensor_old or dist != dist_old:
			if dist<thresh: 
				setRGB(255,0,0) # set backlight to red
				setText(thresh, "cm OBJ PRES")
			else: 
				setRGB(0,255,0) # set backlight to green 
				setText(thresh, "cm")
			setText_norefresh("\n",dist,"cm")
