import fusionengine as fusion

window = fusion.Window("Example: 2", 800, 600)


@window.loop
def loop():
    fusion.set_background_color(fusion.VIOLET)
    fusion.draw_rect(100, 100, 400, 400, fusion.BLUE)

    if fusion.Key(fusion.KEY_a).key_down():
        print("Key A pressed")
