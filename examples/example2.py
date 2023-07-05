import fusionengine as fusion

main = fusion.Main()

window = main.window.new_window("Example: 2", 800, 600)

while main.window.running(window):
    main.draw.set_background_color(window, main.color.WHITE)
    main.draw.draw_rect(window, 100, 100, 400, 400, main.color.BLUE)

    if main.event.key_down(main.keys.KEY_a, window):
        print("Key A pressed")

main.quit(window)
