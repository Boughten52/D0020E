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
            observer.post_event("Fibaro", state)
            time.sleep(1)
    """

    # -------- DEBUG -------- #
    while True:
        #print("DEBUG")
        observer.post_event("Fibaro", "door_42_open")
        time.sleep(1)
    """