import os
import sys
sys.path.append(os.getcwd())
from src.engine import main as engine

main = engine.Main()

window = main.window.newWindow("Hello World", 800, 600)

while main.window.running:
    main.draw.drawLine(window.surface, 0, 0, 800, 600, main.BLUE)
    main.window.refresh(window.window)
    
quit(window)



