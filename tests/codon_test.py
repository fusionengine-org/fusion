from python import fusionengine as fusion


main = fusion.Main()

window = main.window.new_window("Example: 1", 600, 600)
image = main.image.open_image(window, main.debug.DEBUGIMAGE, 0, 0, 600, 600)

while main.window.running(window):
    main.image.draw_image(image)
