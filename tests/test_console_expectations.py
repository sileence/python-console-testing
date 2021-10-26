import pytest
from console_testing.MockConsole import MockConsole

def test_verifies_an_input_expectation():
    test_console = MockConsole()
    test_console.expect_message("My message")

    test_console.print("My message")

    test_console.assert_expectations_met()

def test_verifies_a_question_expectation():
    test_console = MockConsole()
    test_console.expect_question("What's your name?", "Duilio")

    name = test_console.ask("What's your name?")

    assert name == "Duilio", f"The question didn't return the expected name Duilio. It returned: [{name}] instead."
    test_console.assert_expectations_met()

def test_assert_expectations_met_fails_if_one_expectation_is_not_met():
    test_console = MockConsole()
    test_console.expect_message("My message")

    with pytest.raises(AssertionError, match='All the message expectations were not met. Missing 1 expectation.'):
        test_console.assert_expectations_met()

def test_assert_expectations_met_fails_if_two_expectations_are_not_met():
    test_console = MockConsole()
    test_console.expect_message("First message")
    test_console.expect_message("Second message")

    with pytest.raises(AssertionError, match='All the message expectations were not met. Missing 2 expectations.'):
        test_console.assert_expectations_met()

def test_assert_expectations_met_fails_if_all_the_expectations_are_not_met():
    test_console = MockConsole()
    test_console.expect_message("First message")
    test_console.expect_message("Second message")

    test_console.print("First message")

    with pytest.raises(AssertionError, match='All the message expectations were not met. Missing 1 expectation.'):
        test_console.assert_expectations_met()

def test_multiple_expectations_in_the_right_order_will_pass_the_test():
    test_console = MockConsole()\
        .expect_message("Welcome to our app")\
        .expect_question("What's your name?", "Duilio")

    test_console.print("Welcome to our app")
    name = test_console.ask("What's your name?")

    assert name == "Duilio", f"The question didn't return the expected name Duilio. It returned: [{name}] instead."
    test_console.assert_expectations_met()

def test_printing_a_message_with_no_expectations_raises_an_assertion_error():
    test_console = MockConsole()

    with pytest.raises(AssertionError, match='The expectations list is empty'):
        test_console.print("Unexpected message")

def test_asking_a_question_with_no_expectations_raises_an_assertion_error():
    test_console = MockConsole()

    with pytest.raises(AssertionError, match='The expectations list is empty'):
        test_console.ask("What's your favorite song?")

def test_printing_an_unexpected_message_type_raises_an_assertion_error():
    test_console = MockConsole()
    test_console.expect_message("My message")

    with pytest.raises(AssertionError, match="We expected a message but got a question instead."):
        test_console.ask("Unexpected question")

def test_printing_an_unexpected_message_raises_an_assertion_error():
    test_console = MockConsole()
    test_console.expect_message("My message")

    with pytest.raises(AssertionError, match="We expected the message: 'My message' but got 'Unexpected message' instead."):
        test_console.print("Unexpected message")

def test_printing_an_unexpected_question_raises_an_assertion_error():
    test_console = MockConsole()
    test_console.expect_question("What's your favorite TV Series?", "Bojack")

    expected_exception_message = "We expected the message: 'What's your favorite TV Series\?' but got 'What's your favorite Movie\?' instead."

    with pytest.raises(AssertionError, match=expected_exception_message):
        test_console.ask("What's your favorite Movie?")
