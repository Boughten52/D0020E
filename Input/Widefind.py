import paho.mqtt.client as mqtt
import json
import numpy as np
import Observer.ObserverClass
import Logging.log


class WideFind:
    observer = Observer.ObserverClass
    log = Logging.log

    def __init__(self, url: str, port: int):
        self.broker_url = url
        self.broker_port = port

        self.__client = mqtt.Client()
        self.__client.on_connect = self.__on_connect
        self.__client.on_message = self.__on_message

    def run(self) -> None:
        self.__client.connect(self.broker_url, self.broker_port)
        self.__client.loop_start()

        self.__client.subscribe("ltu-system/#")

    def __on_connect(self, client, userdata, flags, rc, properties=None):
        pass

    def __on_message(self, client, userdata, message):
        mqtt_message_str = message.payload.decode("utf-8")
        mqtt_message_json = json.loads(message.payload)
        mqtt_message_list = mqtt_message_json["message"].split(',')
        tracker_id = mqtt_message_list[0][7:]

        if (tracker_id == "F1587D88122BE247"):

            # Get coordinates
            list = mqtt_message_list[2:5]
            vector = np.array([])

            # Convert to int
            for element in list:
                intElement = int(element)
                vector = np.append(vector, intElement)

            lampDoor = np.array([793, -956, 1650])
            distanceDoor = np.subtract(vector, lampDoor)
            distanceDoor = np.linalg.norm(distanceDoor)

            lampTv = np.array([4144, -242, 696])
            distanceTv = np.subtract(vector, lampTv)
            distanceTv = np.linalg.norm(distanceTv)

            lampKitchen = np.array([1029, -5311, 1367])
            distanceKitchen = np.subtract(vector, lampKitchen)
            distanceKitchen = np.linalg.norm(distanceKitchen)

            # print(vector)
            # print("Distance to door: ", distanceDoor)
            # print("Distance to Tv: ", distanceTv)
            # print("Distance to Kitchen: ", distanceKitchen)

            # Door
            if distanceDoor < 1500:
                data = "widefind_1_frontdoor"
                self.observer.post_event("Event", data)
                self.log.write_log_info(data)
            else:
                data = "widefind_1_NOT-frontdoor"
                self.observer.post_event("Event", data)
                self.log.write_log_info(data)

            # Tv
            if distanceTv < 1500:
                data = "widefind_1_livingroom"
                self.observer.post_event("Event", data)
                self.log.write_log_info(data)
            else:
                data = "widefind_1_NOT-livingroom"
                self.observer.post_event("Event", data)
                self.log.write_log_info(data)

            # Kitchen
            if distanceKitchen < 1500:
                data = "widefind_1_kitchen"
                self.observer.post_event("Event", data)
                self.log.write_log_info(data)
            else:
                data = "widefind_1_NOT-kitchen"
                self.observer.post_event("Event", data)
                self.log.write_log_info(data)

        return
