import fusionengine as fusion

main = fusion.Main()

window = main.window.new_window("Example: 3", 800, 600)

player = main.body.Entity("rigid", window, 100, 100, 50, 50)

@main.window.loop
def loop():

    main.draw.set_background_color(window, main.color.WHITE)
    main.draw.draw_rect(window, 100, 100, 400, 400, main.color.BLUE)

main.quit(window)
