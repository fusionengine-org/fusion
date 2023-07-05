import fusionengine as fusion

main = fusion.Main()

window = main.window.new_window("Example: 4", 800, 600)

while main.window.running(window):
    pass

main.quit(window)