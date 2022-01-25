# Från grupp 10

import paho.mqtt.client as mqtt
import json


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

        tracker_id = mqtt_message_list[0][7:]
        print(mqtt_message_json)
        #print(tracker_id)


#widefind = WideFind("130.240.74.55", 1883)
#widefind.run()

#while True:
#    pass
