import os
import sys
sys.path.append(os.getcwd())
from src.engine import main as engine

main = engine.Main()

window = main.window.newWindow("Hello World", 800, 600)

while main.window.running:
    #main.draw.drawLine(window.surface, 0, 0, 800, 600, main.color.BLUE)
    main.draw.drawRect(window, 100, 100, 400, 400, main.color.RED)
    main.window.refresh(window)
    
quit(window)
