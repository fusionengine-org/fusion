import fusionengine as fusion

main = fusion.Main()

window = main.window.new_window("Fusion Engine", 800, 600)

@main.window.loop
def loop():
    main.draw.set_background_color(window, (main.color.BLUE))
    button = main.ui.button.new_button(
        window,
        "Hello World",
        25,
        25,
        200,
        100,
        "default",
        "default",
        0,
        main.color.GREEN,
        lambda:
            print("Hello World")
    )
    # print("loop")
