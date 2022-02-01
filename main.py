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

# -------- READ RULES TO DICTIONARY -------- #
currentUserList = "rules_" + str(config["userinfo"]["user"])
rules = {}
for i in range(0, len(config[currentUserList]["if"])):
    if config[currentUserList]["if"][i] in rules:
        rules[config[currentUserList]["if"][i]].append(config[currentUserList]["then"][i])
    else:
        rules[config[currentUserList]["if"][i]] = [config[currentUserList]["then"][i]]


def event_handler(data):
    if data in rules.keys():
        outputList = rules[data]
        for output in outputList:
            message = output.split("_")
            name = message[0]
            id = int(message[1])
            action = message[2]
            if name == "lamp":
                lights(id, action)
                current_time = datetime.now().strftime("%H:%M:%S")
                print(current_time, ": ", data)


def setup_event_handler():
    observer.subscribe("Event", event_handler)


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
