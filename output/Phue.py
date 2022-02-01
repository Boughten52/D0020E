from phue import Bridge


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
        self.bridge.set_light(light, 'on', True)
        self.lights[light].brightness = 127

    def light_off(self, light):
        self.bridge.set_light(light, 'on', False)

    def change_light(self, r, g, b, light):
        self.lights[light].brightness = 127
        self.lights[light].xy = rgb_to_xy(r, g, b)

    def change_lights(self, r, g, b):
        for light in self.lights:
            light.brightness = 127
            light.xy = rgb_to_xy(r, g, b)
