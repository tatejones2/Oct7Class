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

### Running Streamlit Apps
```bash
# Simple Hello World app
streamlit run hello_streamlit.py

# AI-powered chat app
streamlit run streamlit_app.py
```

### Project Structure
```
.
├── src/                    # Source code
│   ├── __init__.py
│   ├── main.py
│   └── openai_example.py
├── tests/                  # Test files
│   ├── __init__.py
│   ├── test_main.py
│   └── test_openai_example.py
├── docs/                   # Documentation
│   └── streamlit_guide.md
├── streamlit_app.py        # AI chat web app
├── hello_streamlit.py      # Simple Streamlit demo
├── .gitignore             # Git ignore rules
├── requirements.txt       # Production dependencies
├── requirements-dev.txt   # Development dependencies
├── pytest.ini           # pytest configuration
├── pylintrc             # pylint configuration
└── README.md            # This file
```

## Streamlit Apps

This project includes two Streamlit applications:

### 1. Hello Streamlit (`hello_streamlit.py`)
A simple introduction to Streamlit featuring:
- Interactive widgets (sliders, text inputs, buttons)
- Data visualization (charts and tables)
- Basic UI components and layout

### 2. AI Chat App (`streamlit_app.py`)
An AI-powered chat application featuring:
- Real-time chat interface
- OpenAI GPT integration
- Configurable AI parameters
- Session state management
- Sample prompts and chat history

## Usage

This is a starter project. Add your code to the `src/` directory and tests to the `tests/` directory.