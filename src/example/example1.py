import os
import sys
sys.path.append(os.getcwd())
from src.engine import main as engine

main = engine.Main()

window = main.window.newWindow("Example: 1", 800, 600)
image = main.image.openImage(window, main.DEBUGIMAGE, 100, 100, 400, 400)

while main.window.running:
        
    main.image.drawImage(image)

    main.window.refresh(window)

quit(window)
