import sys
sys.path.append("..")
 
from consoletests.MockConsole import MockConsole

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

def test_multiple_expectations_in_the_right_order_will_pass_the_test():
    test_console = MockConsole()\
        .expect_message("Welcome to our app")\
        .expect_question("What's your name?", "Duilio")

    test_console.print("Welcome to our app")
    name = test_console.ask("What's your name?")

    assert name == "Duilio", f"The question didn't return the expected name Duilio. It returned: [{name}] instead."
    test_console.assert_expectations_met()

def test_printing_a_message_with_no_expectations_raises_an_assertion_error():
    try:
        test_console = MockConsole()
        
        test_console.print("Not expected message")
    except AssertionError as error:
        assert 'The expectations list is empty' == str(error)
        return

    assert False, "The expected error was not raised"

def test_printing_a_question_with_no_expectations_raises_an_assertion_error():
    try:
        test_console = MockConsole()
        
        test_console.ask("What's your favorite song?")
    except AssertionError as error:
        assert 'The expectations list is empty' == str(error)
        return

    assert False, "The expected error was not raised"

def test_printing_an_unexpected_message_type_raises_an_assertion_error():
    test_console = MockConsole()
    test_console.expect_message("My message")

    try:
        test_console.ask("Unexpected question")
    except AssertionError as error:
        assert "We expected a message but got a question instead." == str(error)
        return

def test_printing_an_unexpected_message_raises_an_assertion_error():
    test_console = MockConsole()
    test_console.expect_message("My message")

    try:
        test_console.print("Unexpected message")
    except AssertionError as error:
        assert "We expected the message: 'My message' but got 'Unexpected message' instead." == str(error)
        return

def test_printing_an_unexpected_question_raises_an_assertion_error():
    test_console = MockConsole()
    test_console.expect_question("What's your favorite TV Series?", "Bojack")

    try:
        test_console.ask("What's your favorite Movie?")
    except AssertionError as error:
        assert "We expected the message: 'What's your favorite TV Series?' but got 'What's your favorite Movie?' instead." == str(error)
        return