from phue import Bridge

bridge = Bridge('130.240.114.9')

# Connect once and press the connect button on the Pilips Hue bridge at the same time
bridge.connect()

# Might be preferable to get the names instead of id:s
lights = bridge.get_light_objects('id')
lights[1].on = True
lights[1].brightness = 127

print(lights)
