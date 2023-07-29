import fusionengine as fusion

main = fusion.Main()

window = main.window.new_window("Example: 1", 600, 600)
image = main.image.open_image(window, main.debug.DEBUGIMAGE, 0, 0, 600, 600)


@main.window.loop
def loop():
    main.image.draw_image(image)


main.quit(window)
