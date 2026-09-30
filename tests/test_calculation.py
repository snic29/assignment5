import pytest
from typing import Union
from app.operations import Operations
from app.calculation import (
    Calculation,
    CalculationFactory,
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
    PowerCalculation,
)

# Define a type alias for numbers that can be either int or float
Number = Union[int, float]

# ----- ADD CALCULATION TESTS -----
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),            # add_positive_calculation
        (-2, 3, 1),           # add_negative_calculation
        (2.5, 3.5, 6.0),      # add_float_calculation
    ],
    ids=[
        "add_positive_calculation",
        "add_negative_calculation",
        "add_float_calculation",
    ]
)
def test_add_calculation(a: Number, b: Number, expected: Number) -> None:
    calculation = AddCalculation(a, b)
    result = calculation.execute()
    assert result == expected, f"Expected AddCalculation({a}, {b}) to be {expected}, but got {result}"


# ----- SUBTRACT CALCULATION TESTS -----
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),            # subtract_positive_calculation
        (-2, 3, -5),          # subtract_negative_calculation
        (5.5, 2.5, 3.0),      # subtract_float_calculation
    ],
    ids=[
        "subtract_positive_calculation",
        "subtract_negative_calculation",
        "subtract_float_calculation",
    ]
)
def test_subtract_calculation(a: Number, b: Number, expected: Number) -> None:
    calculation = SubtractCalculation(a, b)
    result = calculation.execute()
    assert result == expected, f"Expected SubtractCalculation({a}, {b}) to be {expected}, but got {result}"

# ----- MULTIPLY CALCULATION TESTS -----
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),            # multiply_positive_calculation
        (-2, 3, -6),          # multiply_negative_calculation
        (2.5, 4.0, 10.0),     # multiply_float_calculation
    ],
    ids=[
        "multiply_positive_calculation",
        "multiply_negative_calculation",
        "multiply_float_calculation",
    ]
)
def test_multiply_calculation(a: Number, b: Number, expected: Number) -> None:
    calculation = MultiplyCalculation(a, b)
    result = calculation.execute()
    assert result == expected, f"Expected MultiplyCalculation({a}, {b}) to be {expected}, but got {result}"

# ----- DIVIDE CALCULATION TESTS -----
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2),            # divide_positive_calculation
        (-6, 3, -2),          # divide_negative_calculation
        (7.0, 3.5, 2.0),      # divide_float_calculation
    ],
    ids=[
        "divide_positive_calculation",
        "divide_negative_calculation",
        "divide_float_calculation",
    ]
)
def test_divide_calculation(a: Number, b: Number, expected: Number) -> None:
    calculation = DivideCalculation(a, b)
    result = calculation.execute()
    assert result == expected, f"Expected DivideCalculation({a}, {b}) to be {expected}, but got {result}"

# ----- DIVIDE BY ZERO CALCULATION TESTS -----
@pytest.mark.parametrize(
    "a, b",
    [
        (1, 0),               # divide_positive_integer_by_zero
        (-1, 0),              # divide_negative_integer_by_zero
        (1.2, 0),             # divide_positive_float_by_zero
        (-1.2, 0),            # divide_negative_float_by_zero
        (0, 0),               # divide_zero_by_zero
    ],
    ids=[
        "divide_positive_integer_by_zero",
        "divide_negative_integer_by_zero",
        "divide_positive_float_by_zero",
        "divide_negative_float_by_zero",
        "divide_zero_by_zero",
    ]
)
def test_divide_by_zero(a: Number, b: Number) -> None:
    calculation = DivideCalculation(a, b)

    with pytest.raises(ZeroDivisionError, match="Division by zero is not allowed.") as excinfo:
        calculation.execute()

    assert "Division by zero is not allowed." in str(excinfo.value), \
        f"Expected error message 'Division by zero is not allowed.', but got '{excinfo.value}'"

# ----- POWER CALCULATION TESTS -----
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 0, 1),            # power_to_zero
        (2, 3, 8),            # power_positive_integers
        (-2, 3, -8),          # power_negative_base_odd_exponent
        (-2, 4, 16),          # power_negative_base_even_exponent
        (2.0, 3.0, 8.0),      # power_positive_floats
        (9, 0.5, 3.0),        # power_square_root
    ],
    ids=[
        "power_to_zero",
        "power_positive_integers",
        "power_negative_base_odd_exponent",
        "power_negative_base_even_exponent",
        "power_positive_floats",
        "power_square_root",
    ]
)
def test_power_calculation(a: Number, b: Number, expected: Number) -> None:
    calculation = PowerCalculation(a, b)
    result = calculation.execute()
    assert result == expected, f"Expected PowerCalculation({a}, {b}) to be {expected}, but got {result}"


# ----- CALCULATION STRING REPRESENTATION TESTS -----
@pytest.mark.parametrize(
    "calculation, expected",
    [
        (
            AddCalculation(2, 3),
            "AddCalculation: 2 Add 3 = 5"
        ),
        (
            SubtractCalculation(5, 3),
            "SubtractCalculation: 5 Subtract 3 = 2"
        ),
        (
            MultiplyCalculation(2, 3),
            "MultiplyCalculation: 2 Multiply 3 = 6"
        ),
        (
            DivideCalculation(6, 3),
            "DivideCalculation: 6 Divide 3 = 2.0"
        ),
        (
            PowerCalculation(2, 3),
            "PowerCalculation: 2 Power 3 = 8"
        ),
    ],
    ids=[
        "str_add_calculation",
        "str_subtract_calculation",
        "str_multiply_calculation",
        "str_divide_calculation",
        "str_power_calculation",
    ]
)
def test_calculation_str(calculation: Calculation, expected: str) -> None:
    assert str(calculation) == expected


# ----- CALCULATION REPR TESTS -----
@pytest.mark.parametrize(
    "calculation, expected",
    [
        (
            AddCalculation(2, 3),
            "AddCalculation(a=2, b=3)"
        ),
        (
            SubtractCalculation(-2, 3),
            "SubtractCalculation(a=-2, b=3)"
        ),
        (
            MultiplyCalculation(2.5, 4.0),
            "MultiplyCalculation(a=2.5, b=4.0)"
        ),
        (
            DivideCalculation(6, 3),
            "DivideCalculation(a=6, b=3)"
        ),
        (
            PowerCalculation(2, 3),
            "PowerCalculation(a=2, b=3)"
        ),
    ],
    ids=[
        "repr_add_calculation",
        "repr_subtract_calculation",
        "repr_multiply_calculation",
        "repr_divide_calculation",
        "repr_power_calculation",
    ]
)
def test_calculation_repr(calculation: Calculation, expected: str) -> None:
    assert repr(calculation) == expected


# ----- ABSTRACT CALCULATION TESTS -----
def test_calculation_is_abstract() -> None:
    with pytest.raises(TypeError):
        Calculation(2, 3)


# ----- FACTORY CREATION TESTS -----
@pytest.mark.parametrize(
    "calculation_type, expected_class",
    [
        ("add", AddCalculation),             # factory_create_add
        ("subtract", SubtractCalculation),   # factory_create_subtract
        ("multiply", MultiplyCalculation),   # factory_create_multiply
        ("divide", DivideCalculation),       # factory_create_divide
        ("power", PowerCalculation),         # factory_create_power
    ],
    ids=[
        "factory_create_add",
        "factory_create_subtract",
        "factory_create_multiply",
        "factory_create_divide",
        "factory_create_power",
    ]
)
def test_factory_create_calculation(calculation_type: str, expected_class: type[Calculation]) -> None:
    calculation = CalculationFactory.create_calculation(calculation_type, 6, 3)
    assert isinstance(calculation, expected_class)
    assert calculation.a == 6
    assert calculation.b == 3


# ----- FACTORY CASE-INSENSITIVE TESTS -----
@pytest.mark.parametrize(
    "calculation_type, expected_class",
    [
        ("Add", AddCalculation),             # factory_add_mixed_case
        ("SUBTRACT", SubtractCalculation),   # factory_subtract_uppercase
        ("Multiply", MultiplyCalculation),   # factory_multiply_mixed_case
        ("DIVIDE", DivideCalculation),       # factory_divide_uppercase
        ("Power", PowerCalculation),         # factory_power_mixed_case
    ],
    ids=[
        "factory_add_mixed_case",
        "factory_subtract_uppercase",
        "factory_multiply_mixed_case",
        "factory_divide_uppercase",
        "factory_power_mixed_case",
    ]
)
def test_factory_case_insensitive(calculation_type: str, expected_class: type[Calculation]) -> None:
    calculation = CalculationFactory.create_calculation(calculation_type, 6, 3)
    assert isinstance(calculation, expected_class)


# ----- FACTORY INVALID TYPE TESTS -----
@pytest.mark.parametrize(
    "calculation_type",
    [
        "unknown",              # factory_unknown_type
        "modulus",              # factory_unsupported_operation
        "",                     # factory_empty_type
        "addition",             # factory_invalid_add_type
        "PowerCalculation",     # factory_invalid_class_name
    ],
    ids=[
        "factory_unknown_type",
        "factory_unsupported_operation",
        "factory_empty_type",
        "factory_invalid_add_type",
        "factory_invalid_class_name",
    ]
)
def test_factory_invalid_type(calculation_type: str) -> None:
    with pytest.raises(ValueError, match=f"Unsupported calculation type: '{calculation_type}'") as excinfo:
        CalculationFactory.create_calculation(calculation_type, 2, 3)
    assert calculation_type in str(excinfo.value)


# ----- FACTORY REGISTRATION TESTS -----
def test_register_calculation_returns_subclass() -> None:
    class TestCalculation(Calculation):
        def execute(self) -> float:
            return self.a + self.b

    decorator = CalculationFactory.register_calculation("test")

    registered_class = decorator(TestCalculation)

    assert registered_class is TestCalculation
    assert CalculationFactory._calculations["test"] is TestCalculation

    # Prevent this test from affecting other tests
    del CalculationFactory._calculations["test"]


def test_register_calculation_converts_type_to_lowercase() -> None:
    class TestCalculation(Calculation):
        def execute(self) -> float:
            return self.a + self.b

    CalculationFactory.register_calculation("TEST")(TestCalculation)

    assert "test" in CalculationFactory._calculations
    assert CalculationFactory._calculations["test"] is TestCalculation

    del CalculationFactory._calculations["test"]


def test_register_duplicate_calculation_raises_value_error() -> None:
    class TestCalculation(Calculation):
        def execute(self) -> float:
            return self.a + self.b

    CalculationFactory.register_calculation("duplicate_test")(
        TestCalculation
    )

    with pytest.raises(ValueError, match="Calculation type 'DUPLICATE_TEST' is already registered."):
        CalculationFactory.register_calculation("DUPLICATE_TEST")(TestCalculation)

    del CalculationFactory._calculations["duplicate_test"]
