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
    expectations = [
        ["Your name: ", "George"],
        ["Hello, George."],
        ["What is 2**10? ", "64"],
        ["wrong"],
        ["What is 2**10? ", "1024"],
        ["correct"],
    ]
    return MockConsole.from_iterable(expectations)


def test_simple_script(scripts_in_path, mock_console):
    with mock_console.all_expectations_met():
        import simple_script


def test_script_with_main(scripts_in_path, mock_console):
    with mock_console.all_expectations_met():
        from script_with_main import main
        main()
