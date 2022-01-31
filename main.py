import toml

from Input.Fibaro import Fibaro
from Input.WidefindInput import WideFind
from output.phueOutput import PhueOutput
import Observer.ObserverClass

observer = Observer.ObserverClass

config = toml.load("config.toml")

# Read rules to dictionary
currentUserList = "rules_" + str(config["userinfo"]["user"])
rules = {}
for i in range(0, len(config[currentUserList]["if"])):
    if config[currentUserList]["if"][i] in rules:
        rules[config[currentUserList]["if"][i]].append(config[currentUserList]["then"][i])
    else:
        rules[config[currentUserList]["if"][i]] = [config[currentUserList]["then"][i]]

if config["phue"]["enabled"]:
    print("Using Philips hue")
    phue = PhueOutput(config["phue"]["ip"])

def main():

    setupEventHandler()

    config = toml.load("config.toml")

    if config["widefind"]["enabled"]:
        print("Using WideFind")
        widefind = WideFind(config["widefind"]["ip"], config["widefind"]["port"])
        widefind.run()

    if config["fibaro"]["enabled"]:
        print("Using Fibaro")
        fibaro = Fibaro(config["fibaro"]["ip"], config["fibaro"]["user"], config["fibaro"]["password"])

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
    """
    while True:
        if config["widefind"]["enabled"]:
            widefindStates = widefind.get_state()
            # for state in widefindStates...
        if config["fibaro"]["enabled"]:
            fibaroStates = fibaro.get_state()
            # CONTINUE HERE
        time.sleep(1)
    """
    while True:
        pass


def eventHandler(data):
    if data in rules.keys():
        print("In eventHandler")
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
                    print("IN")
                    phue.lightOff(id)



def setupEventHandler():
    observer.subscribe("Event", eventHandler)


if __name__ == '__main__':
    main()
