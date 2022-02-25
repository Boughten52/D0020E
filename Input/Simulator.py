import time

from Input.Input import Input
from Observer.ObserverClass import Observer


class Simulator(Input):

    observer = Observer()

    def __init__(self):
        pass

    def run(self):
        while True:
            time.sleep(5)
            self.observer.post_event("Event", "door_42_open")
            time.sleep(1)
            self.observer.post_event("Event", "widefind_2_frontdoor")
            time.sleep(3)
            """
            self.observer.post_event("Event", "door_42_closed")
            time.sleep(5)
            self.observer.post_event("Event", "widefind_2_NOT-frontdoor")
            time.sleep(2)
            self.observer.post_event("Event", "widefind_1_kitchen")
            time.sleep(3)
            self.observer.post_event("Event", "door_50_open")
            time.sleep(5)
            self.observer.post_event("Event", "door_50_closed")
            time.sleep(4)
            self.observer.post_event("Event", "door_55_open")
            time.sleep(2)
            self.observer.post_event("Event", "door_55_closed")
            time.sleep(7)
            self.observer.post_event("Event", "door_31_open")
            time.sleep(2)
            self.observer.post_event("Event", "door_31_closed")
            time.sleep(5)
            self.observer.post_event("Event", "widefind_1_NOT-kitchen")
            time.sleep(2)
            self.observer.post_event("Event", "widefind_3_livingroom")
            time.sleep(10)
            self.observer.post_event("Event", "widefind_3_NOT-livingroom")
            time.sleep(2)
            self.observer.post_event("Event", "widefind_1_kitchen")
            time.sleep(5)
            self.observer.post_event("Event", "door_31_open")
            time.sleep(3)
            self.observer.post_event("Event", "door_31_closed")
            time.sleep(6)
            self.observer.post_event("Event", "widefind_1_NOT-kitchen")
            time.sleep(3)
            self.observer.post_event("Event", "widefind_2_frontdoor")
            time.sleep(4)
            self.observer.post_event("Event", "door_42_open")
            time.sleep(3)
            self.observer.post_event("Event", "widefind_2_NOT-frontdoor")
            time.sleep(1)
            self.observer.post_event("Event", "door_42_closed")
            time.sleep(10)
            """
