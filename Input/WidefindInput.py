# Från grupp 10

import paho.mqtt.client as mqtt
import json
import numpy as np

from output.phueOutput import PhueOutput


class WideFind:

    def __init__(self, url: str, port: int):
        self.broker_url = url
        self.broker_port = port

        self.__client = mqtt.Client()
        self.__client.on_connect = self.__on_connect
        self.__client.on_message = self.__on_message

        self.trackers = {}

    def run(self) -> None:
        self.__client.connect(self.broker_url, self.broker_port)
        self.__client.loop_start()

        self.__client.subscribe("ltu-system/#")

    def __on_connect(self, client, userdata, flags, rc, properties=None):
        print("Connected")

    def __on_message(self, client, userdata, message):
        mqtt_message_str = message.payload.decode("utf-8")
        mqtt_message_json = json.loads(message.payload)
        mqtt_message_list = mqtt_message_json["message"].split(',')

        list = mqtt_message_list[2:5]
        vector = np.array([])

        for element in list:
            intElement = int(element)
            vector = np.append(vector, intElement)
        #17C08B1230924C5D
        #xyz
        #['4246' '-654' '614']
        tracker_id = mqtt_message_list[0][7:]
        if (tracker_id == "F1587D88122BE247"):

            print(vector)
            print(tracker_id)
            print(mqtt_message_json)

            if (vector[0] <= 4400 and vector[0] >= 4000):
                print("JA1")
                if (vector[2] <= 700 and vector[2] >= 500):
                    print("JA2")
                    phueObject.changeLights(255, 0, 0)
                    print()

            print()


phueObject = PhueOutput()
phueObject.main()

widefind = WideFind("130.240.74.55", 1883)
widefind.run()

while True:
    pass
