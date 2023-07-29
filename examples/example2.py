import fusionengine as fusion

main = fusion.Main()

window = main.window.new_window("Example: 2", 800, 600)


@main.window.loop
def loop():
    main.draw.set_background_color(window, (main.color.VIOLET))
    main.draw.draw_rect(window, 100, 100, 400, 400, main.color.BLUE)

    if main.event.key_down(main.keys.KEY_a):
        print("Key A pressed")
