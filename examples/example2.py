import fusionengine as fusion

main = fusion.Main()

window = main.window.newWindow("Example: 2", 800, 600)

while main.window.running(window):
    main.draw.setBackgroundColor(window, main.color.WHITE)
    main.draw.drawRect(window, 100, 100, 400, 400, main.color.BLUE)

    if main.event.keyDown(main.keys.KEY_a, window):
        print("Key A pressed")

main.quit(window)
