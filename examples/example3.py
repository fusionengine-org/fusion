import fusionengine as fusion

window = fusion.window.Window("Example: 3", 800, 600)

player = fusion.body.Entity(window, 70, 40, 50, 50)


speed = 10


@window.loop
def loop():
    fusion.draw.set_background_color(window, fusion.color.WHITE)

    player.load_rect(fusion.color.AQUA)

    if fusion.event.key_down(fusion.keys.KEY_UP):
        player.y = int(player.y - speed)

    elif fusion.event.key_down(fusion.keys.KEY_DOWN):
        player.y = int(player.y + speed)

    elif fusion.event.key_down(fusion.keys.KEY_RIGHT):
        player.x = int(player.x + speed)

    elif fusion.event.key_down(fusion.keys.KEY_LEFT):
        player.x = int(player.x - speed)
