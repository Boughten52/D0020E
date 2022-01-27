from abc import ABC, abstractmethod
import json

class Input(ABC):

    @abstractmethod
    def get_input(self) -> (bool, str):
        pass
        