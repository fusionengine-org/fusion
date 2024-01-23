import fusionengine as fusion

window = fusion.Window("Example: 3", 800, 600)

player = fusion.Entity(window, 50, 50, 50, 50)


speed = 10


@window.loop
def loop():
    fusion.set_background_color(fusion.WHITE)

    player.load_rect(fusion.AQUA)

    if fusion.Key(fusion.KEY_UP).key_down() or fusion.Key(fusion.KEY_W).key_down():
        player.y = int(player.y - speed)

    elif fusion.Key(fusion.KEY_DOWN).key_down() or fusion.Key(fusion.KEY_S).key_down():
        player.y = int(player.y + speed)

    elif fusion.Key(fusion.KEY_RIGHT).key_down() or fusion.Key(fusion.KEY_D).key_down():
        player.x = int(player.x + speed)

    elif fusion.Key(fusion.KEY_LEFT).key_down() or fusion.Key(fusion.KEY_A).key_down():
        player.x = int(player.x - speed)

    player.draw_rect()
