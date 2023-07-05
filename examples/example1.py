import fusionengine as fusion

main = fusion.Main()

window = main.window.new_window("Example: 1", 800, 600)
image = main.image.open_image(window, main.DEBUGIMAGE, 100, 100, 400, 400)

@main.window.loop
def loop():

    main.image.draw_image(image)

main.quit(window)
