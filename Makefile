PYTHON = python
PIP = pip
PYINSTALLER = pyinstaller

setup:
	$(PIP) install pysdl2
	$(PIP) install pysdl2-dll
	$(PIP) install pyinstaller
	
example: 
	$(PYTHON) src/example/example.py

test: 
	$(PYTHON) src/test/test1.py

create:
	$(PYINSTALLER) --hidden-import=sdl2 src/example/example.py --workpath build --distpath build/dist --specpath build/spec --onefile --windowed



