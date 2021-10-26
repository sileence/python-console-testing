

from consoletests.Console import Console
from consoletests.Console import Console

class BasicConsole(Console):
    def print(self, message):
        print(message)

    def ask(self, question):
        return input(question)