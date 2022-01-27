import toml

from Input.Fibaro import Fibaro
from Input.WidefindInput import WideFind
from output.phueOutput import PhueOutput


def main():
    config = toml.load("config.toml")

    if config["widefind"]["enabled"]:
        print("Using WideFind")
        widefind = WideFind(config["widefind"]["ip"], config["widefind"]["port"])
        widefind.run()

    if config["fibaro"]["enabled"]:
        print("Using Fibaro")
        #fibaro = Fibaro(config["fibaro"]["ip"], config["fibaro"]["user"], config["fibaro"]["password"])

        # UNCOMMENT TO SEE CURRENTLY OPEN DOORS
        # print("Open doors:")
        # for device in fibaro.getOpenDoors():
        #    print(device.id, device.name)

    if config["phue"]["enabled"]:
        print("Using Philips hue")
        phue = PhueOutput(config["phue"]["ip"])

    # Read rules to dictionary
    currentUserList = "rules_" + str(config["userinfo"]["user"])
    rules = {}
    for i in range(0, len(config[currentUserList]["if"])):
        if config[currentUserList]["if"][i] in rules:
            rules[config[currentUserList]["if"][i]].append(config[currentUserList]["then"][i])
        else:
            rules[config[currentUserList]["if"][i]] = [config[currentUserList]["then"][i]]

    print(rules)

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

    # while True:
    #    pass

if __name__ == '__main__':
    main()

while True:
    pass
