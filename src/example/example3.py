import os
import sys
sys.path.append(os.getcwd())
from src.engine import main as engine

main = engine.Main()

window = main.window.newWindow("Example: 1", 800, 600)

player = main.body.Entity("rigid", window, 100, 100, 50, 50)

while main.window.running:
    main.draw.setBackgroundColor(window, main.color.WHITE)
    main.draw.drawRect(window, 100, 100, 400, 400, main.color.BLUE)

quit(window)