# Python Project

A Python project with virtual environment, testing, and linting setup.

## Features

- Virtual environment management
- pytest with coverage reporting
- pylint for code quality
- OpenAI API integration with python-dotenv
- Pre-configured development environment

## Setup

1. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```

## Development

### Running Tests
```bash
pytest
```

### Running Tests with Coverage
```bash
pytest --cov=src --cov-report=html --cov-report=term
```

### Code Quality
```bash
pylint src/
```

### Project Structure
```
.
├── src/                    # Source code
│   └── __init__.py
├── tests/                  # Test files
│   └── __init__.py
├── .gitignore             # Git ignore rules
├── requirements.txt       # Production dependencies
├── requirements-dev.txt   # Development dependencies
├── pytest.ini           # pytest configuration
├── pylintrc             # pylint configuration
└── README.md            # This file
```

## Usage

This is a starter project. Add your code to the `src/` directory and tests to the `tests/` directory.