import time
from Observer.ObserverClass import Observer
from fiblary3.client import Client


class Fibaro:

    def __init__(self, ip, user, password):
        global observer
        global connection
        observer = Observer()
        connection = Client('v3', ip, user, password)

    def run(self) -> None:

        while True:
            # GET OPEN DOORS
            open_doors = connection.devices.list(
                baseType="com.fibaro.doorWindowSensor",
                jsonpath="$[?(@.properties.value==True)]"
            )

            # GET CLOSED DOORS
            closed_doors = connection.devices.list(
                baseType="com.fibaro.doorWindowSensor",
                jsonpath="$[?(@.properties.value==False)]"
            )

            # ALL CURRENT STATES
            states = []
            for device in open_doors:
                states.append("door_" + str(device.id) + "_open")
            for device in closed_doors:
                states.append("door_" + str(device.id) + "_closed")

            for state in states:
                # print("State", state)
                observer.post_event("Event", state)
            time.sleep(1)

