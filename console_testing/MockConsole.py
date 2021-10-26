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
        assert len(self.expectations) == 0