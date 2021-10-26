class ConsoleExpectation():
    def __init__(self, message_type, message, returns = None):
        self.message_type = message_type
        self.message = message
        self.returns = returns

    def assert_matches(self, actual_message_type, actual_message):
        assert actual_message_type == self.message_type, f"We expected a {self.message_type} but got a {actual_message_type} instead."
        assert actual_message == self.message, f"We expected the message: '{self.message}' but got '{actual_message}' instead."
        return self.returns