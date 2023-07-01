from fusionengine import main as engine

main = engine.Main()

window = main.window.newWindow("Example: 4", 800, 600)

while main.window.running(window):
    pass

main.quit(window)