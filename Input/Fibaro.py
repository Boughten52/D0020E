import time
import Observer.ObserverClass

from fiblary3.client import Client


def run(ip, user, password):
    observer = Observer.ObserverClass
    connection = Client('v3', ip, user, password)

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

