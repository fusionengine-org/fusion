PYTHON = python
PIP = pip

setup:
	$(PIP) install pysdl2
	$(PIP) install pysdl2-dll
	
example: 
	$(PYTHON) src/example/example.py

test: 
	$(PYTHON) src/test/test1.py



