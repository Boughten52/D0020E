from abc import ABC, abstractmethod


class Input(ABC):

    @abstractmethod
    def __init__(self):
        pass

    # Should always notify observers
    @abstractmethod
    def run(self):
        pass
