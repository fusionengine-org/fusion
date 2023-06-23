# Define some variables
EXAMPLE = 1

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
	PYTHON_GLB := python
	PYTHON := $(VENV_PATH)\Scripts\python.exe
	PIP := $(VENV_PATH)\Scripts\pip.exe
	INSTALLER := $(VENV_PATH)\Scripts\cxfreeze.exe
else
	PYTHON_GLB := python
	PYTHON := $(VENV_PATH)/bin/python
	PIP := $(VENV_PATH)/bin/pip
	INSTALLER := $(VENV_PATH)/bin/cxfreeze
endif

# Define targets and recipes
.PHONY: setup example test compile

setup:
	$(PYTHON_GLB) -m venv $(VENV_PATH)
	$(PIP) install -r requirements.txt

example:
	$(PYTHON) src/example/example$(EXAMPLE).py

test:
	$(PYTHON) src/test/test1.py

compile:
	$(PYTHON) build/setup.py build

update:
	$(PIP) uninstall -r requirements.txt
	$(PIP) install -r requirements.txt

