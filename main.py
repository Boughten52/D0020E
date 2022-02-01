import sys
import threading
import os
import toml
import time
import Observer.ObserverClass

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
    #Fibaro.run(config["fibaro"]["ip"], config["fibaro"]["user"], config["fibaro"]["password"])
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


def main():
    setup_event_handler()

    while True:
        pass

    # On message:
    # trigger = message_payload
    # if trigger in rules:
    #     outputList = rules[trigger]
    # for output in outputList:
    #     dispatch (check name, id, action and then dispatch)
    #     if output[name] == "lamp":
    #         if output[action] == "on":
    #             phue.turnOnLamp(output[id])

    # Alternatively:
    # If messages doesn't work, get state every few seconds which contains open doors and sensor position
    # for state in currentStates:
    #     if state in rules:
    #         outputList = rules[state]
    #     for output in outputList:
    #          dispatch (check name, id, action and then dispatch) - REPETITION OF DISPATCHES EVEN IF STATE IS UNCHANGED
    #          if output[name] == "lamp":
    #              if output[action] == "on":
    #                  phue.turnOnLamp(output[id])


    """
    while True:
        if config["widefind"]["enabled"]:
            widefindStates = widefind.get_state()
            # for state in widefindStates...


        if config["fibaro"]["enabled"] == False:
            for state in fibaro_states:
                if state in rules.keys():
                    output_list = rules[state]
                    for output in output_list:
                        data = output.split("_")
                        name = data[0]
                        id = int(data[1])
                        action = data[2]
                        if name == "lamp":
                            if action == "on":
                                phue.light_on(id)
                                phue.changeLight(255, 0, 0, id)
                            if action == "off":
                                phue.light_off(id)
                            if action == "yellow":
                                phue.change_light(255, 0, 0, id)
                            if action == "purple":
                                phue.change_light(255, 0, 255, id)
                            if action == "debug":
                                print("main")

        print("In main")
        time.sleep(1)
        """


def fibaro_event_handler(data):
    print(data)


def widefind_event_handler(data):
    if data in rules.keys():
    outputList = rules[data]
    for output in outputList:
        message = output.split("_")
        name = message[0]
        id = message[1]
        action = message[2]
        if name == "lamp":
            if action == "on":
                phue.change_light(0, 0, 255, int(id))
                print("On")

            if action == "off":
                phue.light_off(int(id))
                #phue.change_lights(200, 0, 255)
                print("off")


def setup_event_handler():
    observer.subscribe("Widefind", widefind_event_handler)
    observer.subscribe("Fibaro", fibaro_event_handler)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
