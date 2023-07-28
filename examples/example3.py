import fusionengine as fusion

main = fusion.Main()

window = main.window.new_window("Example: 3", 800, 600)

player = main.body.Entity("rigid", window, 70, 40, 50, 50)


speed = 10


@main.window.loop
def loop():
    main.draw.set_background_color(window, main.color.WHITE)

    player.new_rect(window, main.color.AQUA)

    if main.event.key_down(main.keys.KEY_UP, window):
        player.y = int(player.y - speed)

    elif main.event.key_down(main.keys.KEY_DOWN, window):
        player.y = int(player.y + speed)

    elif main.event.key_down(main.keys.KEY_RIGHT, window):
        player.x = int(player.x + speed)

    elif main.event.key_down(main.keys.KEY_LEFT, window):
        player.x = int(player.x - speed)


main.quit(window)
