from abc import ABC, abstractmethod

class Console(ABC):
    @abstractmethod
    def print(self, message):
        pass

    @abstractmethod
    def ask(self, question):
        pass