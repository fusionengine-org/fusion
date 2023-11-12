import fusionengine as fusion

window = fusion.Window("Example: 3", 800, 600)

player = fusion.Entity(window, 50, 50, 50, 50)


speed = 10


@window.loop
def loop():
    fusion.set_background_color(window, fusion.WHITE)

    player.load_rect(fusion.AQUA)

    if fusion.key_down(fusion.KEY_UP):
        player.y = int(player.y - speed)

    elif fusion.key_down(fusion.KEY_DOWN):
        player.y = int(player.y + speed)

    elif fusion.key_down(fusion.KEY_RIGHT):
        player.x = int(player.x + speed)

    elif fusion.key_down(fusion.KEY_LEFT):
        player.x = int(player.x - speed)

    player.draw_rect()
