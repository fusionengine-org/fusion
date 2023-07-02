import fusionengine as fusion

main = fusion.Main()

window = main.window.newWindow("Example: 3", 800, 600)

player = main.body.Entity("rigid", window, 100, 100, 50, 50)

while main.window.running(window):
    main.draw.setBackgroundColor(window, main.color.WHITE)
    main.draw.drawRect(window, 100, 100, 400, 400, main.color.BLUE)

main.quit(window)