import pytest

from console_testing import MockConsole


@pytest.fixture
def mock_console():
    console = MockConsole()
    console.expect_question("What's your name? ", "Bob")
    console.expect_message("Hello, Bob")
    return console


def test_context_manager_passes_if_all_expectations_met(mock_console):
    def script():
        name = input("What's your name? ")
        print(f"Hello, {name}")

    with mock_console.all_expectations_met():
        script()


def test_context_manager_fails_if_unexpected_message(mock_console):
    def script():
        name = input("What's your name? ")
        print(f"Welcome, {name}")  # unexpected message

    with pytest.raises(AssertionError, match=r"got 'Welcome, Bob' instead"):
        with mock_console.all_expectations_met():
            script()


def test_context_manager_fails_if_unexpected_question(mock_console):
    def script():
        name = input("What is your name? ")  # unexpected question
        print(f"Hello, {name}")

    with pytest.raises(AssertionError, match=r"got 'What is your name\? ' instead"):
        with mock_console.all_expectations_met():
            script()


def test_context_manager_fails_if_unexpected_message_type(mock_console):
    def script():
        print("This is a message.")  # unexpected message type

    with pytest.raises(AssertionError, match=r"got a message instead"):
        with mock_console.all_expectations_met():
            script()


def test_context_manager_fails_if_actual_more_than_expected(mock_console):
    def script():
        name = input("What's your name? ")
        print(f"Hello, {name}")
        print("Additional message.")

    with pytest.raises(AssertionError, match=r"expectations list is empty"):
        with mock_console.all_expectations_met():
            script()


def test_context_manager_fails_if_actual_less_than_expected(mock_console):
    def script():
        name = input("What's your name? ")

    with pytest.raises(AssertionError, match=r"Missing 1 expectation"):
        with mock_console.all_expectations_met():
            script()
