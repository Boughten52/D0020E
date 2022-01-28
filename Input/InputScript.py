from abc import ABC, abstractmethod
import json


class Input(ABC):

    @abstractmethod
    def get_state(self) -> (bool, str):
        pass