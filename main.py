import sys
import threading
import os
import toml
import time
import Observer.ObserverClass
from datetime import datetime

from Input import Fibaro
from Input.Widefind import WideFind
from Output import Output

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

# -------- READ RULES TO LISTS -------- #
# Rules are stored according to indexing.
# The output is stored at the corresponding index in a different list to the input.
currentUserList = "rules_" + str(config["userinfo"]["user"])
inputName = config[currentUserList]["inputName"]
outputName = config[currentUserList]["outputName"]
outputFunction = config[currentUserList]["outputFunction"]
outputArgument = config[currentUserList]["outputArgument"]


def event_handler(data):
    if data in inputName:
        current_time = datetime.now().strftime("%H:%M:%S.%f:")[:-2]
        print(current_time + ": " + data)
        index_list = []
        i = 0
        for e in inputName:
            if data == e:
                index_list.append(i)
            i = i + 1

        for index in index_list:
            eval("Output." + outputFunction[index])(outputArgument[index])  # eval is unsafe in a way


def setup_event_handler():
    observer.subscribe("Event", event_handler)


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
