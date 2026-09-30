from abc import ABC, abstractmethod
from app.operations import Operations

# -----------------------------------------------------------------------------------
# Abstract Base Class: Calculation
# -----------------------------------------------------------------------------------
class Calculation(ABC):
    """
    The Calculation class is an Abstract Base Class (ABC) that defines a blueprint 
    for all mathematical calculations in the calculator program. This class establishes 
    a consistent interface that all calculation types (such as addition, subtraction, etc.) 
    must follow. 
    """

    def __init__(self, a: float, b: float) -> None:
        """Initializes a Calculation instance with two operands"""
        self.a: float = a
        self.b: float = b

    @abstractmethod
    def execute(self) -> float:
        """
        Abstract method to perform the calculation. Subclasses will provide specific 
        implementations of this method, defining the arithmetic for each operation.
        """
        pass  # pragma: no cover

    def __str__(self) -> str:
        """
        Provides a user-friendly string representation of the Calculation instance, 
        showing the operation name, operands, and result.
        """
        result = self.execute()  # Run the calculation to get the result
        operation_name = self.__class__.__name__.replace('Calculation', '')  # Derive operation name
        return f"{self.__class__.__name__}: {self.a} {operation_name} {self.b} = {result}"

    def __repr__(self) -> str:
        """
        Provides a technical, unambiguous representation of the Calculation instance 
        showing the class name and operand values.
        """
        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"

# -----------------------------------------------------------------------------------
# Factory Class: CalculationFactory
# -----------------------------------------------------------------------------------
class CalculationFactory:
    """
    The CalculationFactory is a Factory Class responsible for creating instances 
    of Calculation subclasses. This design pattern allows us to encapsulate the 
    logic of object creation and make it flexible.
    """

    # _calculations is a dictionary that holds a mapping of calculation types 
    # (like "add" or "subtract") to their respective classes
    _calculations = {}

    @classmethod
    def register_calculation(cls, calculation_type: str):
        """
        This method is a decorator used to register a specific Calculation subclass 
        under a unique calculation type. Registering classes with string identifiers 
        like "add" or "multiply" enables easy access to different operations 
        dynamically at runtime.
        """
        def decorator(subclass):
            calculation_type_lower = calculation_type.lower()
            
            # Check if the calculation type has already been registered to avoid duplication
            if calculation_type_lower in cls._calculations:
                raise ValueError(f"Calculation type '{calculation_type}' is already registered.")
            
            # Register the subclass in the _calculations dictionary
            cls._calculations[calculation_type_lower] = subclass

            return subclass  # Return the subclass for chaining or additional use
        return decorator  # Return the decorator function

    @classmethod
    def create_calculation(cls, calculation_type: str, a: float, b: float) -> Calculation:
        """
        Factory method that creates instances of Calculation subclasses based on 
        a specified calculation type.
        """
        calculation_type_lower = calculation_type.lower()
        calculation_class = cls._calculations.get(calculation_type_lower)

        # If the type is unsupported, raise an error with the available types
        if not calculation_class:
            available_types = ', '.join(cls._calculations.keys())
            raise ValueError(f"Unsupported calculation type: '{calculation_type}'. Available types: {available_types}")
        
        # Create and return an instance of the requested calculation class with the provided operands
        return calculation_class(a, b)

# -----------------------------------------------------------------------------------
# Concrete Calculation Classes
# -----------------------------------------------------------------------------------

# Each of these classes defines a specific calculation type (addition, subtraction, 
# multiplication, division, or power). These classes inherit from Calculation, 
# implementing the 'execute' method to perform the specific arithmetic operation. 

@CalculationFactory.register_calculation('add')
class AddCalculation(Calculation):
    """
    AddCalculation represents an addition operation between two numbers
    """
    def execute(self) -> float:
        return Operations.addition(self.a, self.b)

@CalculationFactory.register_calculation('subtract')
class SubtractCalculation(Calculation):
    """
    SubtractCalculation represents a subtraction operation between two numbers
    """
    def execute(self) -> float:
        return Operations.subtraction(self.a, self.b)

@CalculationFactory.register_calculation('multiply')
class MultiplyCalculation(Calculation):
    """
    MultiplyCalculation represents a multiplication operation between two numbers
    """
    def execute(self) -> float:
        return Operations.multiplication(self.a, self.b)

@CalculationFactory.register_calculation('divide')
class DivideCalculation(Calculation):
    """
    DivideCalculation represents a division operation between two numbers
    """
    def execute(self) -> float:
        # Before performing division, check if b is zero to avoid ZeroDivisionError
        if self.b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return Operations.division(self.a, self.b)

@CalculationFactory.register_calculation('power')
class PowerCalculation(Calculation):
    """
    PowerCalculation represents a power operation between two numbers
    """
    def execute(self) -> float:
        return Operations.power(self.a, self.b)