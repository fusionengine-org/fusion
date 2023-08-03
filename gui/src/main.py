import fusionengine as fusion

main = fusion.Main()

window = main.window.new_window("Fusion Engine", 800, 600)

# Create the button outside the loop
button = main.ui.button.new_button(
    window,
    main.shape.new_rect_button(200, 200, 200, 200),
    "Hello World"
)

@main.window.loop
def loop():
    main.draw.set_background_color(window, (main.color.BLUE))

    if button.button_pressed():
        print("Hello World")

