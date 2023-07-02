import fusionengine as fusion

main = fusion.Main()

window = main.window.newWindow("Example: 4", 800, 600)

while main.window.running(window):
    pass

main.quit(window)