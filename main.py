import toml
import time

from Input.Fibaro import Fibaro
from Input.WidefindInput import WideFind
from output.phueOutput import PhueOutput
import Observer.ObserverClass

observer = Observer.ObserverClass


config = toml.load("config.toml")

if config["phue"]["enabled"]:
    phue = PhueOutput(config["phue"]["ip"])
    print("Philips hue connected")

# Read rules to dictionary
currentUserList = "rules_" + str(config["userinfo"]["user"])
rules = {}
for i in range(0, len(config[currentUserList]["if"])):
    if config[currentUserList]["if"][i] in rules:
        rules[config[currentUserList]["if"][i]].append(config[currentUserList]["then"][i])
    else:
        rules[config[currentUserList]["if"][i]] = [config[currentUserList]["then"][i]]


def main():

    setupEventHandler()

    if config["widefind"]["enabled"]:
        widefind = WideFind(config["widefind"]["ip"], config["widefind"]["port"])
        widefind.run()
        print("WideFind connected")

    if config["fibaro"]["enabled"]:
        fibaro = Fibaro(config["fibaro"]["ip"], config["fibaro"]["user"], config["fibaro"]["password"])
        print("Fibaro connected")

        # UNCOMMENT TO SEE CURRENTLY OPEN DOORS
        # print("Open doors:")
        # for device in fibaro.getOpenDoors():
        #    print(device.id, device.name)


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
    while True:
        #if config["widefind"]["enabled"]:
            #widefindStates = widefind.get_state()
            # for state in widefindStates...

        if config["fibaro"]["enabled"]:
            fibaro_states = fibaro.get_state()
            #fibaro_states = fibaro.get_state_debug() # FOR DEBUG
            for state in fibaro_states:
                if state in rules.keys():
                    output_list = rules[state]
                    for output in output_list:
                        data = output.split("_")
                        name = data[0]
                        id = data[1]
                        action = data[2]
                        if name == "lamp":
                            if action == "on":
                                phue.changeLight(255, 0, 0, id)

        time.sleep(1)


def eventHandler(data):
    if data in rules.keys():
        outputList = rules[data]
        for output in outputList:
            message = output.split("_")
            name = message[0]
            id = message[1]
            action = message[2]
            if name == "lamp":
                if action == "on":
                    phue.changeLight(0, 0, 255, int(id))
                if action == "off":
                    print("off")
                    #phue.changeLight(255, 0, 255, int(id))
                    phue.lightOff(int(id))
                    print("off")



def setupEventHandler():
    observer.subscribe("Event", eventHandler)


if __name__ == '__main__':
    main()