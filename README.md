# 🧮 Command-Line Calculator

This is a simple Python command-line calculator with a REPL interface supporting addition, subtraction, multiplication, division, and exponentiation.

---

# 🛠️ 1. Project Setup

## Clone the Repository

Clone the GitHub repository and navigate into the project directory:

```bash
git clone <repository-url>
cd <repository-directory>
```

## Install Python

- **MacOS (Homebrew)**

```bash
brew install python
```

- **Windows**

Download and install [Python for Windows](https://www.python.org/downloads/).  
✅ Make sure you **check the box** `Add Python to PATH` during setup.

**Verify Python:**

```bash
python3 --version
```
or
```bash
python --version
```

---

## Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate.bat  # Windows
```

## Install Required Packages
```bash
pip install -r requirements.txt
```

# 🚀 2. Running the Calculator

Start the calculator:

```bash
python3 main.py
```

After starting, the calculator displays a welcome message and waits for commands:

```bash
Welcome to the Professional Calculator REPL!
Type 'help' for instructions or 'exit' to quit.

>>
```

Enter an operation followed by two numbers:

```bash
add 5 3
subtract -10 4
multiply 2.5 4
divide 10 2
power 2 3
```

The calculator supports:
- **`add`**
- **`subtract`**
- **`multiply`**
- **`divide`**
- **`power`**

The calculator handles invalid input, unknown operations, and division by zero with appropriate error messages.

# 📜 3. Special Commands

- **`help`** - Displays usage instructions and the list of supported operations
- **`history`** - Displays all successful calculations performed during the current session
- **`exit`** - Exits the calculator

# 🧪 4. Running Tests

Run all tests:

```bash
pytest
```

Parameterized tests are used in tests/test_operations.py to efficiently test multiple input scenarios.

# ⚙️ 4. GitHub Actions

GitHub Actions automatically runs the test suite when code is pushed to the repository.

The CI workflow:
- Runs all pytest tests.
- Measures test coverage.
- Requires 100% test coverage.
- Fails if any test fails or coverage is below 100%.

# 📁 5. Project Structure

```text
calculator/
├── app/
│   ├── calculation/
│   │   └── __init__.py
│   ├── calculator/
│   │   └── __init__.py
│   │── operations/
│   │    └── __init__.py
│   └── __init__.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_caculation.py
│   ├── test_caculator.py
│   └── test_operations.py
├── .github/workflows/
│   └── tests.yml
├── requirements.txt
├── main.py
└── README.md

```