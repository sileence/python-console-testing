from contextlib import contextmanager
from unittest.mock import patch

from console_testing.ConsoleExpectation import ConsoleExpectation
from console_testing.Console import Console

class MockConsole(Console):
    def __init__(self):
        self.expectations = []

    def expect_message(self, message):
        self.expectations.append(ConsoleExpectation('message', message))
        return self

    def expect_question(self, question, returns):
        self.expectations.append(ConsoleExpectation('question', question, returns))
        return self

    def print(self, message):
        return self.check_expectation('message', message)
        
    def ask(self, question):
        return self.check_expectation('question', question)

    def check_expectation(self, message_type, message):
        assert len(self.expectations) > 0, "The expectations list is empty"
        return self.expectations.pop(0).assert_matches(message_type, message)

    def assert_expectations_met(self):
        expectation_text = 'expectation' if len(self.expectations) == 1 else 'expectations'

        assert len(self.expectations) == 0, f"All the message expectations were not met. Missing {len(self.expectations)} {expectation_text}."

    @contextmanager
    def all_expectations_met(self):
        with patch.multiple('builtins', print=self.print, input=self.ask):
            yield self
        self.assert_expectations_met()

    @classmethod
    def from_iterable(cls, iterable):
        console = cls()
        for item in iterable:
            if len(item) == 1:
                console.expect_message(*item)
            elif len(item) == 2:
                console.expect_question(*item)
        return console
