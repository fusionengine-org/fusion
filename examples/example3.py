import os
import sys
sys.path.append(os.getcwd())
from engine import main as engine

main = engine.Main()

window = main.window.newWindow("Example: 3", 800, 600)

player = main.body.Entity("rigid", window, 100, 100, 50, 50)

while main.window.running(window):
    main.draw.setBackgroundColor(window, main.color.WHITE)
    main.draw.drawRect(window, 100, 100, 400, 400, main.color.BLUE)

main.quit(window)