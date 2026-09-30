""" tests/test_calculator.py """
import pytest
from io import StringIO
from app.calculator import calculator, display_help, display_history

# ----- CALCULATOR TESTS -----

# Positive Tests
def test_addition(monkeypatch, capsys):
    """Test addition operation in REPL."""
    user_input = 'add 2 3\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()
    assert "Result: AddCalculation: 2.0 Add 3.0 = 5.0" in captured.out


def test_subtraction(monkeypatch, capsys):
    """Test subtraction operation in REPL."""
    user_input = 'subtract 5 2\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()
    assert "Result: SubtractCalculation: 5.0 Subtract 2.0 = 3.0" in captured.out


def test_multiplication(monkeypatch, capsys):
    """Test multiplication operation in REPL."""
    user_input = 'multiply 4 5\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()
    assert "Result: MultiplyCalculation: 4.0 Multiply 5.0 = 20.0" in captured.out


def test_division(monkeypatch, capsys):
    """Test division operation in REPL."""
    user_input = 'divide 10 2\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()
    assert "Result: DivideCalculation: 10.0 Divide 2.0 = 5.0" in captured.out


# Negative Tests
def test_invalid_operation(monkeypatch, capsys):
    """Test invalid operation in REPL."""
    user_input = 'modulus 5 3\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()
    assert "Unsupported calculation type: 'modulus'." in captured.out
    assert "Type 'help' to see the list of supported operations." in captured.out


def test_invalid_input_format(monkeypatch, capsys):
    """Test invalid input format in REPL."""
    user_input = 'add two three\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()
    assert "Invalid input. Please ensure numbers are valid." in captured.out or \
           "could not convert string to float: 'ten'" in captured.out or \
           "Invalid input. Please follow the format: <operation> <num1> <num2>" in captured.out


def test_division_by_zero(monkeypatch, capsys):
    """Test division by zero in REPL."""
    user_input = 'divide 10 0\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()
    assert "Cannot divide by zero." in captured.out

# ----- DISPLAY TESTS -----

def test_display_help(capsys):
    """
    Test the display_help function to ensure it prints the correct help message.
    """
    display_help()
    captured = capsys.readouterr()
    expected_output = """
        Calculator REPL Help
        --------------------
        Usage:
            <operation> <number1> <number2>
            - Perform a calculation with the specified operation and two numbers.
            - Supported operations:
                add       : Adds two numbers.
                subtract  : Subtracts the second number from the first.
                multiply  : Multiplies two numbers.
                divide    : Divides the first number by the second.
                power     : Raises the first number to the power of the second.

        Special Commands:
            help      : Display this help message.
            history   : Show the history of calculations.
            exit      : Exit the calculator.

        Examples:
            add 10 5
            subtract 15.5 3.2
            multiply 7 8
            divide 20 4
            power 2 3
    """
    # Remove leading/trailing whitespace for comparison
    assert captured.out.strip() == expected_output.strip()


def test_display_history_empty(capsys):
    """
    Test the display_history function when the history is empty.
    """
    history = []
    display_history(history)
    captured = capsys.readouterr()
    assert captured.out.strip() == "No calculations performed yet."


def test_display_history_with_entries(capsys):
    """
    Test the display_history function when there are entries in the history.
    """
    history = [
        "AddCalculation: 10.0 Add 5.0 = 15.0",
        "SubtractCalculation: 20.0 Subtract 3.0 = 17.0",
        "MultiplyCalculation: 7.0 Multiply 8.0 = 56.0",
        "DivideCalculation: 20.0 Divide 4.0 = 5.0"
    ]
    display_history(history)

    captured = capsys.readouterr()
    expected_output = """Calculation History:
1. AddCalculation: 10.0 Add 5.0 = 15.0
2. SubtractCalculation: 20.0 Subtract 3.0 = 17.0
3. MultiplyCalculation: 7.0 Multiply 8.0 = 56.0
4. DivideCalculation: 20.0 Divide 4.0 = 5.0"""
    assert captured.out.strip() == expected_output.strip()


# ----- COMMAND TESTS -----

def test_calculator_help_command(monkeypatch, capsys):
    """
    Test the calculator function's ability to handle the 'help' command.
    """
    user_input = 'help\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()
    assert "Calculator REPL Help" in captured.out
    assert "Exiting calculator. Goodbye!" in captured.out

def test_calculator_exit(monkeypatch, capsys):
    """
    Test the calculator function's ability to handle the 'exit' command.
    """
    user_input = 'exit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit) as exc_info:
        calculator()

    captured = capsys.readouterr()
    assert "Exiting calculator. Goodbye!" in captured.out
    assert exc_info.type == SystemExit
    assert exc_info.value.code == 0 

def test_calculator_history(monkeypatch, capsys):
    """
    Test the calculator's ability to display calculation history.
    """
    user_input = 'add 10 5\nsubtract 20 3\nhistory\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()
    assert "Result: AddCalculation: 10.0 Add 5.0 = 15.0" in captured.out
    assert "Result: SubtractCalculation: 20.0 Subtract 3.0 = 17.0" in captured.out
    assert "Calculation History:" in captured.out
    assert "1. AddCalculation: 10.0 Add 5.0 = 15.0" in captured.out
    assert "2. SubtractCalculation: 20.0 Subtract 3.0 = 17.0" in captured.out


# ----- EXCEPTION/ERROR TESTS -----

def test_calculator_unexpected_exception(monkeypatch, capsys):
    """
    Test the calculator's handling of unexpected exceptions during calculation execution.
    """
    class MockCalculation:
        def execute(self):
            raise Exception("Mock exception during execution")
        def __str__(self):
            return "MockCalculation"

    def mock_create_calculation(operation, a, b):
        return MockCalculation()

    monkeypatch.setattr('app.calculation.CalculationFactory.create_calculation', mock_create_calculation)
    user_input = 'add 10 5\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()
    assert "An error occurred during calculation: Mock exception during execution" in captured.out
    assert "Please try again." in captured.out


def test_calculator_keyboard_interrupt(monkeypatch, capsys):
    """
    Test the calculator's handling of KeyboardInterrupt (Ctrl+C)
    """
    def mock_input(prompt):
        raise KeyboardInterrupt()
    monkeypatch.setattr('builtins.input', mock_input)

    with pytest.raises(SystemExit) as exc_info:
        calculator()

    captured = capsys.readouterr()
    assert "\nKeyboard interrupt detected. Exiting calculator. Goodbye!" in captured.out
    assert exc_info.value.code == 0


def test_calculator_eof_error(monkeypatch, capsys):
    """
    Test the calculator's handling of EOFError (Ctrl+D)
    """
    def mock_input(prompt):
        raise EOFError()
    monkeypatch.setattr('builtins.input', mock_input)

    with pytest.raises(SystemExit) as exc_info:
        calculator()

    captured = capsys.readouterr()
    assert "\nEOF detected. Exiting calculator. Goodbye!" in captured.out
    assert exc_info.value.code == 0