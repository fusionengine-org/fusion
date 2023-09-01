import fusionengine as fusion

main = fusion.Main()

window = main.window.new_window("Example: 1", 600, 600)
image = main.image.open_image(window, main.debug.DEBUGIMAGE, 0, 0, 600, 600)


@main.window.loop
def loop():
    main.window.set_fps(60)
    if main.event.key_down_once(main.keys.KEY_a):
        print("A was pressed once!")

    main.image.draw_image(image)
