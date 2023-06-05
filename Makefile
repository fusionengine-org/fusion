PYTHON = python

example: src/example/example.py
	$(PYTHON) $^

test: 
	$(PYTHON) src/test/test1.py



