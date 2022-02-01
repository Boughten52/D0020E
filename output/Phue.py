from phue import Bridge
import random


def rgb_to_xy(red, green, blue):
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


class Phue:

    def __init__(self, ip):
        # Connect once and press the connect button on the Pilips Hue bridge at the same time
        self.bridge = Bridge(ip)
        self.bridge.connect()
        self.lights = self.bridge.get_light_objects('id')

    def light_on(self, light):
        if not self.bridge.get_light(light, 'on'):
            self.bridge.set_light(light, 'on', True)
            self.lights[light].brightness = 255
            print("Light: ", light, " turned on")

    def light_off(self, light):
        if self.bridge.get_light(light, 'on'):
            self.bridge.set_light(light, 'on', False)
            print("Light: ", light, " turned off")

    def change_light(self, r, g, b, light):
        if not self.bridge.get_light(light, 'on'):
            self.light_on(light)
            self.lights[light].brightness = 255
            self.lights[light].xy = rgb_to_xy(r, g, b)
            print("Light: ", light, " changed color")

    def change_lights(self, r, g, b):
        for light in self.lights:
            if not self.bridge.get_light(light, 'on'):
                self.light_on(light)
                light.brightness = 255
                light.xy = rgb_to_xy(r, g, b)
                print("Light: ", light, " changed color")

    # ADD FOR ALL LIGHTS AND LOOP
    def disco(self, light):
        self.light_on(light)
        if self.bridge.get_light(light, 'on'):
            self.lights[light].xy = [random.random(), random.random()]
            print("DISCO!!")
