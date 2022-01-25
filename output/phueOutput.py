import random
from time import sleep

from phue import Bridge

bridge = Bridge('130.240.114.9')
#bridge = Bridge('130.240.114.26') Fel

# Connect once and press the connect button on the Pilips Hue bridge at the same time
bridge.connect()

print("HEJ")

print("Hello")

# Might be preferable to get the names instead of id:s
#lights = bridge.get_light_objects('id')
#{13: <phue.Light object "Hue color light 1" at 0x7ffa10ab4fd0>, 14: <phue.Light object "Hue color light 2" at 0x7ffa10ad05d0>, 15: <phue.Light object "Hue color light 3" at 0x7ffa138a5950>}

#Tak ovanför dörr
#lights[13].on = True
while True:
	lights = bridge.get_light_objects()
	for light in lights:
		light.brightness = 254
		light.xy = [random.random(),random.random()]
	sleep(10)

#Tak ovanför mikro
lights[14].on = True
lights[14].brightness = 255

#Lampa på tvbänken
lights[15].on = True
lights[15].brightness = 0

print(lights)
