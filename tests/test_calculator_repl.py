import datetime
from pathlib import Path
import pandas as pd
import pytest
from unittest.mock import Mock, patch, PropertyMock
from decimal import Decimal
from tempfile import TemporaryDirectory
from app.calculator import Calculator
from app.calculator_repl import calculator_repl
from app.calculator_config import CalculatorConfig
from app.exceptions import OperationError, ValidationError
from app.history import LoggingObserver, AutoSaveObserver
from app.operations import OperationFactory

@patch('builtins.input', side_effect=['exit'])
@patch('builtins.print')
def test_calculator_repl_exit(mock_print, mock_input):
    with patch('app.calculator.Calculator.save_history') as mock_save_history:
        calculator_repl()
        mock_save_history.assert_called_once()
        mock_print.assert_any_call("History saved successfully.")
        mock_print.assert_any_call("Goodbye!")

# Test exception while saving history during exit
@patch('builtins.input', side_effect=['exit'])
@patch('builtins.print')
def test_calculator_repl_exit_save_error(mock_print, mock_input):
    with patch('app.calculator.Calculator.save_history', side_effect=Exception("Save failed")):
        calculator_repl()

    mock_print.assert_any_call("Warning: Could not save history: Save failed")
    mock_print.assert_any_call("Goodbye!")

@patch('builtins.input', side_effect=['help', 'exit'])
@patch('builtins.print')
def test_calculator_repl_help(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("\nAvailable commands:")

@patch('builtins.input', side_effect=['add', '2', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_addition(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("\nResult: 5")

@patch('builtins.input', side_effect=['history', 'exit'])
@patch('builtins.print')
def test_calculator_repl_empty_history(mock_print, mock_input):
    with patch('app.calculator.Calculator.show_history', return_value=[]):
        calculator_repl()

    mock_print.assert_any_call("No calculations in history")

@patch('builtins.input', side_effect=['add', '2', '3', 'history', 'exit'])
@patch('builtins.print')
def test_calculator_repl_history(mock_print, mock_input):
    calculator_repl()

    mock_print.assert_any_call("\nCalculation History:")

@patch('builtins.input', side_effect=['clear', 'exit'])
@patch('builtins.print')
def test_calculator_repl_clear(mock_print, mock_input):
    with patch('app.calculator.Calculator.clear_history') as mock_clear:
        calculator_repl()

        mock_clear.assert_called_once()
        mock_print.assert_any_call("History cleared")

@patch('builtins.input', side_effect=['undo', 'exit'])
@patch('builtins.print')
def test_calculator_repl_undo_success(mock_print, mock_input):
    with patch('app.calculator.Calculator.undo', return_value=True):
        calculator_repl()

    mock_print.assert_any_call("Operation undone")

@patch('builtins.input', side_effect=['undo', 'exit'])
@patch('builtins.print')
def test_calculator_repl_undo_nothing(mock_print, mock_input):
    with patch('app.calculator.Calculator.undo', return_value=False):
        calculator_repl()

    mock_print.assert_any_call("Nothing to undo")

@patch('builtins.input', side_effect=['redo', 'exit'])
@patch('builtins.print')
def test_calculator_repl_redo_success(mock_print, mock_input):
    with patch('app.calculator.Calculator.redo', return_value=True):
        calculator_repl()

    mock_print.assert_any_call("Operation redone")

@patch('builtins.input', side_effect=['redo', 'exit'])
@patch('builtins.print')
def test_calculator_repl_redo_nothing(mock_print, mock_input):
    with patch('app.calculator.Calculator.redo', return_value=False):
        calculator_repl()

    mock_print.assert_any_call("Nothing to redo")

@patch('builtins.input', side_effect=['save', 'exit'])
@patch('builtins.print')
def test_calculator_repl_save(mock_print, mock_input):
    with patch('app.calculator.Calculator.save_history') as mock_save_history:
        calculator_repl()

        # Called once for "save" and once for "exit"
        assert mock_save_history.call_count == 2

    mock_print.assert_any_call("History saved successfully")

# Test exception while explicitly using the save command
@patch('builtins.input', side_effect=['save', 'exit'])
@patch('builtins.print')
def test_calculator_repl_save_error(mock_print, mock_input):
    with patch('app.calculator.Calculator.save_history', side_effect=Exception("Save failed")):
        calculator_repl()

    mock_print.assert_any_call("Error saving history: Save failed")

@patch('builtins.input', side_effect=['load', 'exit'])
@patch('builtins.print')
def test_calculator_repl_load(mock_print, mock_input):
    with patch('app.calculator.Calculator.load_history') as mock_load_history:
        calculator_repl()

    mock_load_history.assert_called()
    mock_print.assert_any_call("History loaded successfully")

# Test exception while loading history
@patch('builtins.input', side_effect=['load', 'exit'])
@patch('builtins.print')
def test_calculator_repl_load_error(mock_print, mock_input):
    with patch('app.calculator.Calculator.load_history', side_effect=Exception("Load failed")):
        calculator_repl()

    mock_print.assert_any_call("Error loading history: Load failed")

@patch('builtins.input', side_effect=['add', 'cancel', 'exit'])
@patch('builtins.print')
def test_calculator_repl_cancel_first_number(mock_print, mock_input):
    calculator_repl()

    mock_print.assert_any_call("Operation cancelled")

@patch('builtins.input', side_effect=['add', '2', 'cancel', 'exit'])
@patch('builtins.print')
def test_calculator_repl_cancel_second_number(mock_print, mock_input):
    calculator_repl()

    mock_print.assert_any_call("Operation cancelled")

@patch('builtins.input', side_effect=['divide', '10', '0', 'exit'])
@patch('builtins.print')
def test_calculator_repl_operation_error(mock_print, mock_input):
    calculator_repl()

    assert any(
        "Error:" in str(call)
        for call in mock_print.call_args_list
    )

@patch('builtins.input', side_effect=['add', 'abc', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_validation_error(mock_print, mock_input):
    calculator_repl()

    assert any(
        "Error:" in str(call)
        for call in mock_print.call_args_list
    )

# Test non-Decimal result branch
@patch('builtins.input', side_effect=['add', '2', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_non_decimal_result(mock_print, mock_input):
    with patch('app.calculator.Calculator.perform_operation', return_value=5):
        calculator_repl()

    mock_print.assert_any_call("\nResult: 5")

# Test unexpected exception during an operation
@patch('builtins.input', side_effect=['add', '2', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_unexpected_operation_error(mock_print, mock_input):
    with patch('app.calculator.Calculator.perform_operation', side_effect=Exception("Unexpected operation failure")):
        calculator_repl()

    mock_print.assert_any_call("Unexpected error: Unexpected operation failure")

@patch('builtins.input', side_effect=['unknown', 'exit'])
@patch('builtins.print')
def test_calculator_repl_unknown_command(mock_print, mock_input):
    calculator_repl()

    mock_print.assert_any_call("Unknown command: 'unknown'. Type 'help' for available commands.")

@patch('builtins.input', side_effect=KeyboardInterrupt)
@patch('builtins.print')
def test_calculator_repl_keyboard_interrupt(mock_print, mock_input):
    # First input raises KeyboardInterrupt. The REPL catches it and
    # continues, so the next input needs to eventually terminate it.
    mock_input.side_effect = [KeyboardInterrupt, 'exit']

    calculator_repl()

    mock_print.assert_any_call("\nOperation cancelled")

@patch('builtins.input', side_effect=EOFError)
@patch('builtins.print')
def test_calculator_repl_eof_error(mock_print, mock_input):
    calculator_repl()

    mock_print.assert_any_call("\nInput terminated. Exiting...")

# Test unexpected exception in the main command-processing loop
@patch('builtins.input', side_effect=['help', 'exit'])
@patch('builtins.print')
def test_calculator_repl_unexpected_command_error(mock_print, mock_input):
    with patch('app.calculator.Calculator.show_history', side_effect=Exception("Unexpected command failure")):
        
        # Trigger the history command instead of help
        mock_input.side_effect = ['history', 'exit']

        calculator_repl()

    mock_print.assert_any_call("Error: Unexpected command failure")

@patch('builtins.print')
@patch('app.calculator_repl.Calculator')
def test_calculator_repl_initialization_error(mock_calculator, mock_print):
    mock_calculator.side_effect = Exception("Initialization failed")

    with pytest.raises(Exception, match="Initialization failed"):
        calculator_repl()

    mock_print.assert_any_call("Fatal error: Initialization failed")