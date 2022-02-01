import sys
import threading
import os
import toml
import time
import Observer.ObserverClass
from datetime import datetime

from Input import Fibaro
from Input.WidefindInput import WideFind
from output.Phue import Phue

# -------- INITIALIZE GLOBAL VARIABLES/OBJECTS -------- #
observer = Observer.ObserverClass
config = toml.load("config.toml")

# -------- INSTANTIATE WIDEFIND -------- #
if config["widefind"]["enabled"]:
    widefind = WideFind(config["widefind"]["ip"], config["widefind"]["port"])
    widefind.run()
    print("WideFind connected")

# -------- START FIBARO LOOP AS THREAD -------- #
if config["fibaro"]["enabled"]:
    fibaroThread = threading.Thread(
        target=Fibaro.run,
        args=[config["fibaro"]["ip"], config["fibaro"]["user"], config["fibaro"]["password"]])
    fibaroThread.start()
    # Fibaro.run(config["fibaro"]["ip"], config["fibaro"]["user"], config["fibaro"]["password"])
    print("Fibaro connected")

# -------- INSTANTIATE PHUE -------- #
if config["phue"]["enabled"]:
    phue = Phue(config["phue"]["ip"])
    print("Philips hue connected")

# -------- READ RULES TO ... -------- #
currentUserList = "rules_" + str(config["userinfo"]["user"])
inputName = config[currentUserList]["inputName"]
outputName = config[currentUserList]["outputName"]
outputFunction = config[currentUserList]["outputFunction"]
outputArgument = config[currentUserList]["outputArgument"]

def event_handler(data):
    if data in inputName:
        current_time = datetime.now().strftime("%H:%M:%S")
        print(current_time, ": ", data)
        indexList = []
        i = 0
        for e in inputName:
            if data == e:
                indexList.append(i)
            i = i + 1

        for index in indexList:
            eval(outputFunction[index])(outputArgument[index])  # eval is unsafe in a way



def setup_event_handler():
    observer.subscribe("Event", event_handler)


def generalFunction(outputArgument):
    message = outputArgument.split("_")
    name = message[0]
    id = int(message[1])
    action = message[2]
    if name == "lamp":
        lights(id, action)

def lights(id, action):
    if action == "on":
        phue.light_on(id)
    if action == "off":
        phue.light_off(id)
    if action == "yellow":
        phue.change_light(255, 0, 0, id)
    if action == "purple":
        phue.change_light(255, 0, 255, id)
    if action == "blue":
        phue.change_light(0, 0, 255, id)
    if action == "disco":
        phue.disco(id)


def main():
    setup_event_handler()

    while True:
        time.sleep(1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
