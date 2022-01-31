# Från grupp 10

import paho.mqtt.client as mqtt
import json
import numpy as np
import Observer.ObserverClass


class WideFind:

    observer = Observer.ObserverClass

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
        print("Connected")

    def zone(self, vector) -> None:

        """
        vectorm = [-741, -188, -353]
        vectork = [1279, -193, 164]
        noll = (vector[0] - vectorm[0]) * (vectork[0] - vectorm[0])
        ett = (vector[1] - vectorm[1]) * (vectork[1] - vectorm[1])
        två = (vector[2] - vectorm[2]) * (vectork[2] - vectorm[2])
        tot = noll + ett + två

        noll1 = (vectork[0] - vectorm[0])**2
        ett2 = (vectork[1] - vectorm[1])**2
        två3 = (vectork[2] - vectorm[2])**2
        tot1 = np.sqrt(noll1 + ett2 + två3)

        total = tot / tot1
        """

        """"
        v1 = [-744, -217, -409]
        v2 = [-1256,  -116,  2022]
        va = [v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2]]

        print("Första: ", va)

        v3 = [5606, -6114, 86]
        v4 = [5473, -5831, 2484]
        vb = [v3[0] - v4[0], v3[1] - v4[1], v3[2] - v4[2]]

        print("Andra: ", vb)

        noll1 = (va[0]) ** 2
        ett2 = (va[1]) ** 2
        två3 = (va[2]) ** 2
        tota = np.sqrt(noll1 + ett2 + två3)

        noll = (vb[0]) ** 2
        ett = (vb[1]) ** 2
        två = (vb[2]) ** 2
        totb = np.sqrt(noll + ett + två)

        print("Storlek a: ", tota)
        print("Storlek b: ", totb)

        tot0 = va[0] * vb[0] + va[1] * vb[1] + va[2] * vb[2]
        cos = tot0/(tota*totb)

        print("cos: ", cos)

        vinkel = np.arccos(cos)

        print("Vinkel: ", vinkel)



        #[-744. -217. -409.]
        #[-1256.  -116.  2022.]

        #[ 5606. -6114.    86.]
        #[ 5473. -5831.  2484.]

        #Noll
        #[-261.  363. 2613.]
        #[-145.  466. 2678.]

        #return total
        """

    def __on_message(self, client, userdata, message):
        mqtt_message_str = message.payload.decode("utf-8")
        mqtt_message_json = json.loads(message.payload)
        mqtt_message_list = mqtt_message_json["message"].split(',')
        tracker_id = mqtt_message_list[0][7:]

        if (tracker_id == "F1587D88122BE247"):

            #Get coordinates
            list = mqtt_message_list[2:5]
            vector = np.array([])

            #Convert to int
            for element in list:
                intElement = int(element)
                vector = np.append(vector, intElement)

            lampDoor = np.array([793, -956, 1650])
            distanceDoor = np.subtract(vector, lampDoor)
            distanceDoor = np.linalg.norm(distanceDoor)

            print("hej")
            """
            lampTv = np.array([4144, -242, 696])
            distanceTv = np.subtract(vector, lampTv)
            distanceTv = np.linalg.norm(distanceTv)

            
            lampKitchen = np.array([4144, -242, 696])
            distanceKitchen = np.subtract(vector, lampKitchen)
            distanceKitchen = np.linalg.norm(distanceKitchen)
            """

            print("Distance to door: " + distanceDoor)
            #print("Distance to Tv: " + distanceTv)
            #print("Distance to Kitchen: " + distanceKitchen)
            print(vector)

            #Door
            if distanceDoor < 1500:
                data = "widefind_1_dörr"
                self.observer.post_event("Event", data)


            """
            #If you stand at the tv bench
            if (vector[0] <= 4400 and vector[0] >= 4000):
                if (vector[2] <= 700 and vector[2] >= 500):
                    data = "widefind_1_tv-bänk"
                    self.observer.post_event("Event", data)


            else:
                data = "widefind_1_icke-tv-bänk"
                self.observer.post_event("Event", data)
"""

            # If you stand at the door
            # if (vector[0] <= 1400 and vector[0] >= 1000):
            #     print("in 1")
            #    if (vector[2] <= 1800 and vector[2] >= 1400):
            #        print("in 2")
            #        data = "widefind_1_dörr"
            #        self.observer.post_event("Event", data)


            #else:
             #   data = "widefind_1_icke-dörr"
              #  self.observer.post_event("Event", data)



        return





        """
        list = mqtt_message_list[2:5]
        vector = np.array([])

        for element in list:
            intElement = int(element)
            vector = np.append(vector, intElement)
        
        tracker_id = mqtt_message_list[0][7:]
        if (tracker_id == "F1587D88122BE247"):

            print(vector)
            print(self.zone(vector))
            print(tracker_id)
            print(mqtt_message_json)

            # Kök: 15
            if (vector[0] <= 4400 and vector[0] >= 4000):
                print("JA1")
                if (vector[2] <= 700 and vector[2] >= 500):
                    print("JA2")
                    phueObject.changeLights(255, 0, 255, 15)
                    print()
            else:
                phueObject.lightOff(15)

            #Tvbänken: 14 Funkar
            if (vector[0] <= 4400 and vector[0] >= 4000):
                if (vector[2] <= 700 and vector[2] >= 500):
                    phueObject.changeLights(255, 0, 255, 14)
                    print()
            else:
                phueObject.lightOff(14)

            # Dörr: 13
            if (vector[0] <= 4400 and vector[0] >= 4000):
                print("JA1")
                if (vector[2] <= 700 and vector[2] >= 500):
                    print("JA2")
                    phueObject.changeLights(255, 0, 255, 15)
                    print()

            print()


phueObject = PhueOutput("130.240.114.9")

widefind = WideFind("130.240.74.55", 1883)
"""
