import time
import Observer.ObserverClass

from fiblary3.client import Client


def run(ip, user, password):
    observer = Observer.ObserverClass
    connection = Client('v3', ip, user, password)

    while True:
        # GET OPEN DOORS
        openDoors = connection.devices.list(
            baseType="com.fibaro.doorWindowSensor",
            jsonpath="$[?(@.properties.value==True)]")

        # ALL CURRENT STATES
        states = []
        for device in openDoors:
            states.append("door_" + str(device.id) + "_open")

        for state in states:
            print("State", state)
            observer.post_event("Event", state)
            time.sleep(1)
