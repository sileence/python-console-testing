from pathlib import Path
import sys

import pytest

from console_testing import MockConsole


@pytest.fixture
def scripts_in_path():
    """Fixture to temporarily add `tests/scripts` to import path."""
    scripts_dir = Path(__file__).parent / "scripts"
    sys.path.append(str(scripts_dir))
    yield
    # clean-up
    sys.path.remove(str(scripts_dir))


@pytest.fixture
def mock_console():
    console = MockConsole()
    console.expect_question("Your name: ", "George")
    console.expect_message("Hello, George.")
    console.expect_question("What is 2**10? ", "64")
    console.expect_message("wrong")
    console.expect_question("What is 2**10? ", "1024")
    console.expect_message("correct")
    return console


def test_simple_script(scripts_in_path, mock_console):
    with mock_console.all_expectations_met():
        import simple_script


def test_script_with_main(scripts_in_path, mock_console):
    with mock_console.all_expectations_met():
        from script_with_main import main
        main()
