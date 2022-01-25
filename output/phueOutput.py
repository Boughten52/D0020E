import random
from time import sleep

from phue import Bridge

class PhueOutput:
	bridge = Bridge('130.240.114.9')

	def main(self) -> None:
		# Connect once and press the connect button on the Pilips Hue bridge at the same time
		self.bridge.connect()
		#self.changeLights(self, 255, 0, 0)

	# Might be preferable to get the names instead of id:s
	#lights = bridge.get_light_objects('id')
	#{13: <phue.Light object "Hue color light 1" at 0x7ffa10ab4fd0>, 14: <phue.Light object "Hue color light 2" at 0x7ffa10ad05d0>, 15: <phue.Light object "Hue color light 3" at 0x7ffa138a5950>}

	#Tak ovanför dörr
	#lights[13].on = True

	def rgb_to_xy(self, red, green, blue):

		# gamma correction
		red = pow((red + 0.055) / (1.0 + 0.055), 2.4) if red > 0.04045 else (red / 12.92)
		green = pow((green + 0.055) / (1.0 + 0.055), 2.4) if green > 0.04045 else (green / 12.92)
		blue = pow((blue + 0.055) / (1.0 + 0.055), 2.4) if blue > 0.04045 else (blue / 12.92)

		# convert rgb to xyz
		x = red * 0.649926 + green * 0.103455 + blue * 0.197109
		y = red * 0.234327 + green * 0.743075 + blue * 0.022598
		z = green * 0.053077 + blue * 1.035763

		# convert xyz to xy
		x = x / (x + y + z)
		y = y / (x + y + z)

		return [x, y]

	def changeLights(self, r, g, b, light):
		lights = self.bridge.get_light_objects()
		lights[light]
		lights[light].brightness = 255
		lights[light].xy = self.rgb_to_xy(r, g, b)

	"""
	def changeLights(self, r, g, b, light):
		lights = self.bridge.get_light_objects()
		for light in lights:
			print(lights)
			light.brightness = 255
			light.xy = self.rgb_to_xy(r, g, b)
	"""

	""""
	#Tak ovanför dörr
	lights[13].on = True
	lights[13].brightness = 255
	
	#Tak ovanför mikro
	lights[14].on = True
	lights[14].brightness = 255
	
	#Lampa på tvbänken
	lights[15].on = True
	lights[15].brightness = 255
	"""
