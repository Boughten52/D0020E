import sys
import threading
import os
import toml
import time
from datetime import datetime

from Input.Simulator import Simulator
from Observer.ObserverClass import Observer
from Input.Fibaro import Fibaro
from Input.Widefind import WideFind
from Output.Output import Output


class Main:

    current_states = []

    def __init__(self):
        # -------- INITIALIZE GLOBAL VARIABLES/OBJECTS -------- #
        global observer
        global output
        observer = Observer()
        output = Output()
        config = toml.load("config.toml")
        config_rules = toml.load("config_rules.toml")

        # -------- INSTANTIATE SIMULATOR -------- #
        if config_rules["simulator"]["enabled"]:
            simulator = Simulator()
            simulatorThread = threading.Thread(target=simulator.run)
            simulatorThread.start()

        # -------- INSTANTIATE WIDEFIND -------- #
        if config["widefind"]["enabled"]:
            global widefind
            widefind = WideFind(config["widefind"]["ip"], config["widefind"]["port"])
            widefind.run()
            print("WideFind connected")

        # -------- START FIBARO LOOP AS THREAD -------- #
        if config["fibaro"]["enabled"]:
            global fibaro
            fibaro = Fibaro(config["fibaro"]["ip"], config["fibaro"]["user"], config["fibaro"]["password"])
            fibaroThread = threading.Thread(target=fibaro.run)
            fibaroThread.start()
            # Fibaro.run(config["fibaro"]["ip"], config["fibaro"]["user"], config["fibaro"]["password"])
            print("Fibaro connected")

        # -------- PLACE FURTHER INPUT INITIALIZATIONS HERE -------- #

        # -------- READ RULES TO LISTS -------- #
        # Rules are stored according to indexing.
        # The output is stored at the corresponding index in a different list to the input.
        currentUserList = str(config_rules["userinfo"]["currentRule"])
        global inputName
        global outputName
        global outputFunction
        global outputArgument
        inputName = config_rules[currentUserList]["inputName"]
        outputName = config_rules[currentUserList]["outputName"]
        outputFunction = config_rules[currentUserList]["outputFunction"]
        outputArgument = config_rules[currentUserList]["outputArgument"]

    def event_handler(self, data):
        if data in self.current_states:
            return

        splitData = data.split("_")
        name = splitData[0]
        id = splitData[1]
        nameAndId = name + "_" + id
        for state in self.current_states:
            if state.startswith(nameAndId):
                self.current_states.remove(state)
                break

        current_time = datetime.now().strftime("%H:%M:%S.%f:")[:-2]
        print(current_time + ": " + data)

        self.current_states.append(data)

        # Only try to dispatch output if there exists a rule
        if data in inputName:
            self.dispatch_output(data)

        # Check for combined input
        self.find_combined_input(data)

    @staticmethod
    def dispatch_output(data):
        index_list = []
        i = 0
        for e in inputName:
            if data == e:
                index_list.append(i)
            i = i + 1

        for index in index_list:
            eval("output." + outputFunction[index])(outputArgument[index])  # eval is unsafe in a way

    def find_combined_input(self, data):
        for status in inputName:
            if data + "&" in status or "&" + data in status:
                split_inputs = status.split("&")
                if all(item in self.current_states for item in split_inputs):
                    self.dispatch_output(status)

    def setup_event_handler(self):
        observer.subscribe("Event", self.event_handler)

    def main(self):
        self.setup_event_handler()

        while True:
            time.sleep(1)


m = Main()
if __name__ == '__main__':
    try:
        m.main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
