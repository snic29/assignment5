import pytest
from typing import Union
from app.operations import Operations

# Define a type alias for numbers that can be either int or float
Number = Union[int, float]

# ----- ADDITION UNIT TESTS -----
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (0, 0, 0),          # add_two_zeros
        (2, 3, 5),          # add_two_positive_integers
        (-2, -3, -5),       # add_two_negative_integers
        (-2, 3, 1),         # add_negative_and_positive_integer
        (2.2, 3.8, 6.0),    # add_two_positive_floats
        (-2.2, -3.8, -6.0), # add_two_negative_floats
        (-2.2, 3.2, 1.0),   # add_negative_float_and_positive_float
        (2, 3.2, 5.2),      # add_positive_int_and_positive_float
        (-2, 3.0, 1.0)      # add_negative_int_and_positive_float
    ],
    ids=[
        "add_two_zeros",
        "add_two_positive_integers",
        "add_two_negative_integers",
        "add_negative_and_positive_integer",
        "add_two_positive_floats",
        "add_two_negative_floats",
        "add_negative_float_and_positive_float",
        "add_positive_int_and_positive_float",
        "add_negative_int_and_positive_float",
    ]
)
def test_addition(a: Number, b: Number, expected: Number) -> None:
    result = Operations.addition(a, b)
    assert result == expected, f"Expected addition({a}, {b}) to be {expected}, but got {result}"

# ----- SUBTRACTION UNIT TESTS -----
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (0, 0, 0),          # subtract_two_zeros
        (5, 3, 2),          # subtract_two_positive_integers
        (-2, -3, 1),        # subtract_two_negative_integers
        (3, -2, 5),         # subtract_negative_integer_from_positive_integer
        (6.0, 3.8, 2.2),    # subtract_two_positive_floats
        (-2.5, -3.5, 1.0),  # subtract_two_negative_floats
        (3.2, -2.2, 5.4),   # subtract_negative_float_from_positive_float
        (3.0, 2, 1.0),      # subtract_positive_int_from_positive_float
        (3.2, -2, 5.2)      # subtract_negative_int_from_positive_float
    ],
    ids=[
        "subtract_two_zeros",
        "subtract_two_positive_integers",
        "subtract_two_negative_integers",
        "subtract_negative_integer_from_positive_integer",
        "subtract_two_positive_floats",
        "subtract_two_negative_floats",
        "subtract_negative_float_from_positive_float",
        "subtract_positive_int_from_positive_float",
        "subtract_negative_int_from_positive_float",
    ]
)
def test_subtraction(a: Number, b: Number, expected: Number) -> None:
    result = Operations.subtraction(a, b)
    assert result == expected, f"Expected subtraction({a}, {b}) to be {expected}, but got {result}"

# ----- MULTIPLICATION UNIT TESTS -----
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (0, 8, 0),          # multiply_positive_integer_by_zero
        (5, 3, 15),         # multiply_two_positive_integers
        (-2, -3, 6),        # multiply_two_negative_integers
        (3, -2, -6),        # multiply_negative_integer_and_positive_integer
        (2.0, 3.5, 7.0),    # multiply_two_positive_floats
        (-2.0, -3.5, 7.0),  # multiply_two_negative_floats
        (-2.0, 3.5, -7.0),  # multiply_negative_float_and_positive_float
        (3, 2.5, 7.5),      # multiply_positive_int_and_positive_float
        (-3, -2.5, 7.5)     # multiply_negative_int_and_positive_float
    ],
    ids=[
        "multiply_positive_integer_by_zero",
        "multiply_two_positive_integers",
        "multiply_two_negative_integers",
        "multiply_negative_integer_and_positive_integer",
        "multiply_two_positive_floats",
        "multiply_two_negative_floats",
        "multiply_negative_float_and_positive_float",
        "multiply_positive_int_and_positive_float",
        "multiply_negative_int_and_positive_float",
    ]
)
def test_multiplication(a: Number, b: Number, expected: Number) -> None:
    result = Operations.multiplication(a, b)
    assert result == expected, f"Expected multiplication({a}, {b}) to be {expected}, but got {result}"

# ----- DIVISION UNIT TESTS -----
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (0, 8, 0),          # divide_zero_by_positive_integer
        (6, 3, 2),          # divide_two_positive_integers
        (-6, -3, 2),        # divide_two_negative_integers
        (6, -2, -3),        # divide_negative_integer_by_positive_integer
        (7.0, 3.5, 2.0),    # divide_two_positive_floats
        (-7.0, -3.5, 2.0),  # divide_two_negative_floats
        (7.0, -3.5, -2.0),  # divide_negative_float_by_positive_float
        (7, 3.5, 2.0),      # divide_positive_int_by_positive_float
        (-7, 3.5, -2.0)     # divide_negative_int_by_positive_float
    ],
    ids=[
        "divide_zero_by_positive_integer",
        "divide_two_positive_integers",
        "divide_two_negative_integers",
        "divide_negative_integer_by_positive_integer",
        "divide_two_positive_floats",
        "divide_two_negative_floats",
        "divide_negative_float_by_positive_float",
        "divide_positive_int_by_positive_float",
        "divide_negative_int_by_positive_float",
    ]
)
def test_division(a: Number, b: Number, expected: Number) -> None:
    result = Operations.division(a, b)
    assert result == expected, f"Expected division({a}, {b}) to be {expected}, but got {result}"

# ----- DIVISION BY ZERO UNIT TESTS -----
@pytest.mark.parametrize(
    "a, b",
    [
        (1, 0),             # divide_positive_integer_by_zero
        (-1, 0),            # divide_negative_integer_by_zero
        (1.2, 0),           # divide_positive_float_by_zero
        (-1.2, 0),          # divide_negative_float_by_zero
        (0, 0)              # divide_zero_by_zero
    ],
    ids=[
        "divide_positive_integer_by_zero",
        "divide_negative_integer_by_zero",
        "divide_positive_float_by_zero",
        "divide_negative_float_by_zero",
        "divide_zero_by_zero",
    ]
)
def test_division_by_zero(a: Number, b: Number) -> None:

    # Use pytest's context manager to check for a ValueError when dividing by zero
    with pytest.raises(ValueError, match="Division by zero is not allowed.") as excinfo:
        Operations.division(a, b)
    
    # Assert the exception message contains the expected error message
    assert "Division by zero is not allowed." in str(excinfo.value), \
        f"Expected error message 'Division by zero is not allowed.', but got '{excinfo.value}'"

# ----- POWER UNIT TESTS -----
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 0, 1),          # power_to_zero
        (2, 3, 8),          # power_two_positive_integers
        (-2, 3, -8),        # power_negative_base_odd_exponent
        (-2, 4, 16),        # power_negative_base_even_exponent
        (2.0, 3.0, 8.0),    # power_two_positive_floats
        (-2.0, 3.0, -8.0),  # power_negative_float_odd_exponent
        (-2.0, 4.0, 16.0),  # power_negative_float_even_exponent
        (9, 0.5, 3.0)       # power_sqrt
    ],
    ids=[
        "power_to_zero",
        "power_two_positive_integers",
        "power_negative_base_odd_exponent",
        "power_negative_base_even_exponent",
        "power_two_positive_floats",
        "power_negative_float_odd_exponent",
        "power_negative_float_even_exponent",
        "power_sqrt"
    ]
)
def test_power(a: Number, b: Number, expected: Number) -> None:
    result = Operations.power(a, b)
    assert result == expected, f"Expected power({a}, {b}) to be {expected}, but got {result}"
