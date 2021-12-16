from console_testing import MockConsole


def test_from_iterable():
    expectations_list = [
        ["What's the time? ", "2 p.m."],
        ["Good afternoon!"],
    ]
    console = MockConsole.from_iterable(expectations_list)
    with console.all_expectations_met():
        answer = input("What's the time? ")
        print("Good morning!" if "a.m." in answer else "Good afternoon!")
