import time

from Input.Input import Input
from Observer.ObserverClass import Observer


class Simulator(Input):

    observer = Observer()

    def __init__(self):
        pass

    def run(self):
        while True:
            states = ["door_42_open", "door_42_closed"]

            self.observer.post_event("Event", states[0])
            time.sleep(1)
            self.observer.post_event("Event", states[0])
            time.sleep(1)
            self.observer.post_event("Event", states[0])
            time.sleep(1)
            self.observer.post_event("Event", states[0])
            time.sleep(1)
            self.observer.post_event("Event", states[1])
            time.sleep(1)
            self.observer.post_event("Event", states[1])
            time.sleep(1)
            self.observer.post_event("Event", states[1])
            time.sleep(1)
            self.observer.post_event("Event", states[1])
            time.sleep(1)
            self.observer.post_event("Event", states[1])
            time.sleep(1)
            self.observer.post_event("Event", states[1])
            time.sleep(1)
            self.observer.post_event("Event", states[1])
            time.sleep(1)
            self.observer.post_event("Event", states[1])
            time.sleep(1)
            self.observer.post_event("Event", states[1])
            time.sleep(1)

