import sys
import threading
import os
import toml
import time
from datetime import datetime

from Observer.ObserverClass import Observer
from Input.Fibaro import Fibaro
from Input.Widefind import WideFind
from Output.Output import Output

class Main:

    def __init__(self):
        # -------- INITIALIZE GLOBAL VARIABLES/OBJECTS -------- #
        global observer
        global output
        observer = Observer()
        output = Output()
        config = toml.load("config.toml")

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
            fibaroThread = threading.Thread(
                target=fibaro.run)
            fibaroThread.start()
            # Fibaro.run(config["fibaro"]["ip"], config["fibaro"]["user"], config["fibaro"]["password"])
            print("Fibaro connected")

        # -------- READ RULES TO LISTS -------- #
        # Rules are stored according to indexing.
        # The output is stored at the corresponding index in a different list to the input.
        currentUserList = "rules_" + str(config["userinfo"]["user"])
        global inputName
        global outputName
        global outputFunction
        global outputArgument
        inputName = config[currentUserList]["inputName"]
        outputName = config[currentUserList]["outputName"]
        outputFunction = config[currentUserList]["outputFunction"]
        outputArgument = config[currentUserList]["outputArgument"]


    def event_handler(self, data):
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
                eval("output." + outputFunction[index])(outputArgument[index])  # eval is unsafe in a way


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
