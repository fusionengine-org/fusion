# Define the operating system
ifeq ($(OS),Windows_NT)
    DETECTED_OS := Windows
else
    UNAME_S := $(shell uname -s)
    ifeq ($(UNAME_S),Linux)
        DETECTED_OS := Linux
    endif
    ifeq ($(UNAME_S),Darwin)
        DETECTED_OS := macOS
    endif
endif

# Set up virtual environment paths based on the operating system
VENV_PATH := venv
ifeq ($(DETECTED_OS),Windows)
    PYTHON := $(VENV_PATH)\Scripts\python.exe
    PIP := $(VENV_PATH)\Scripts\pip.exe
    PYINSTALLER := $(VENV_PATH)\Scripts\pyinstaller.exe
else
    PYTHON := $(VENV_PATH)/bin/python
    PIP := $(VENV_PATH)/bin/pip
    PYINSTALLER := $(VENV_PATH)/bin/pyinstaller
endif

PYTHON_CMD := $(shell command -v python 2> /dev/null)
ifeq ($(strip $(PYTHON_CMD)),)
    PYTHON_CMD := python3
endif

# Define targets and recipes
.PHONY: setup example test create

setup:
    $(PYTHON_CMD) -m venv $(VENV_PATH)
    $(PIP) install -r requirements.txt

example:
    $(PYTHON) src/example/example.py

test:
    $(PYTHON) src/test/test1.py

create:
    $(PYINSTALLER) --hidden-import=sdl2 src/example/example.py --workpath build --distpath build/dist --specpath build/spec --onefile --windowed
