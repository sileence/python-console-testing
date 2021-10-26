# Console Testing

This is a basic Python Package to help programming students write tests for Python exercises that interact with the console.

In other words, you will be able to write expressive tests with *unitest* or *pytest* with scripts that require the use of functions like `input` or `print`.

## Installation

You can install the Console Testing Package running:

`pip install console_testing`

## How to use

Instead of using `print()` and `input()`, you will use the `print` and `ask` methods available in the `BasicConsole` and `MockConsole` classes:

## Basic Console Class

The basic console class is a very simple implementation of `Console` that will forward any call to the normal `print()` and `input()` Python functions:

```
console = BasicConsole()
console.print('A message') # equivalent of print('A message')
console.ask('A question') # equivalent of input('A question')
```

## Mock Console Class

The mock console class is another implementation of `Console` that you can use when running your tests.

However, when using a `MockConsole` object, you need to define the messages and questions that you expect before calling `print` and `ask`, otherwise an `AssertionError` will be raised, causing your tests to fail.

In this way you can ensure that your script is working correctly within the context of a unit test.

For example:

```
console = MockConsole()

# Expects that the console would print the message "A message"
console.expect_message('A message')

# Expect that the console would print the question "A question" and return the answer "An answer"
console.expect_question('A question', 'An answer')

console.print('A message') # equivalent of print('A message')
console.ask('A question') # equivalent of input('A question')

console.assert_expectations_met()
```

Notice how we first expect the message "A message" and then we expect the question "A question". Then we proceed to printing and asking those messages in the expected order - An `AssertionError` will be triggered if we call them in the wrong order.

At the end, we can call `console.assert_expectations_met()` to verify all the expected messages and questions were called.

## Full Example Usage

I advice you to "encapsulate" your scripts in a class or a function and then pass the right console you want to use:

- `BasicConsole` if you want to test by manually running your script in the console/terminal.
- `MockConsole` when you want to test your script within a unit test or pytest.

### Example with function

A function (in our example, `my_script`) will have the logic of your script as you'd normally write it, with the only difference that you will call `console.print` and `console.ask` instead of `print()` and `input()`.

```
from console_testing import BasicConsole, MockConsole

def my_script(console): 
    console.print('Hello from console')
    name = console.ask("What's your name? ")
    console.print(f"Welcome to Python, {name}")

# Using My Command with a BasicConsole Object will run basic print() and input() calls.
basic_console = BasicConsole()

my_script(basic_console)

# Using My Command with a MockConsole Object won't output anything to the console,
# instead it will verify expectations for print() and input() function calls,
# so you can easily write integration tests for simple console programs.
mock_console = MockConsole()
mock_console.expect_message('Hello from console')\
    .expect_question("What's your name? ", 'Duilio')\
    .expect_message('Welcome to Python, Duilio')

my_script(mock_console)

mock_console.assert_expectations_met()
```

### Intermediate example with Class

You can also use a class and "inject" the `Console` as a dependency.

The class `MyCommand` has 2 methods:

- `__init__` is the constructor that we will use to pass and set the console in the `console` property.
- `handle` will have the logic of your script as you'd normally write it, with the only difference that you will call `self.console.print` and `self.console.ask` instead of `print()` and `input()`.

```
from console_testing import BasicConsole, MockConsole

# Define the class MyCommand that will hold the logic of the script
class MyCommand(): 
    def __init__(self, console) -> None:
        self.console = console

    def handle(self):
        self.console.print('Hello from console')
        name = self.console.ask("What's your name? ")
        self.console.print(f"Welcome to Python, {name}")

# Using My Command with a BasicConsole Object will run basic print() and input() calls.
basic_console = BasicConsole()
my_command = MyCommand(basic_console)
my_command.handle()

# Using My Command with a MockConsole Object won't output anything to the console,
# instead it will verify expectations for print() and input() function calls,
# so you can easily write integration tests for simple console programs.
mock_console = MockConsole()
mock_console.expect_message('Hello from console')\
    .expect_question("What's your name? ", 'Duilio')\
    .expect_message('Welcome to Python, Duilio')

my_command = MyCommand(mock_console)
my_command.handle()

mock_console.assert_expectations_met()
```