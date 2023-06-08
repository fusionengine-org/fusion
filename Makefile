PYTHON_GLB = python
PYTHON = venv/bin/python
PIP = venv/bin/pip
PYINSTALLER = pyinstaller

setup:
	$(PYTHON_GLB) -m venv venv
	$(PIP) install -r requirements.txt
	
example: 
	$(PYTHON) src/example/example.py

test: 
	$(PYTHON) src/test/test1.py

create:
	$(PYINSTALLER) --hidden-import=sdl2 src/example/example.py --workpath build --distpath build/dist --specpath build/spec --onefile --windowed



