from fiblary3.client import Client
import paho.mqtt.client as mqtt
import json


class Fibaro:

    def __init__(self, ip, user, password):
        self.connection = Client('v3', ip, user, password)

    def getOpenDoors(self):
        openDoors = self.connection.devices.list(
            baseType = "com.fibaro.doorWindowSensor",
            jsonpath="$[?(@.properties.value==True)]")
        return openDoors

    def get_state(self):
        state = []
        openDoors = self.getOpenDoors()
        for device in openDoors:
            state.append("door_" + str(device.id) + "_open")
        return state