import fusionengine as fusion

window = fusion.Window("Example: 2", 800, 600)


@window.loop
def loop():
    fusion.set_background_color(window, (fusion.VIOLET))
    fusion.draw_rect(window, 100, 100, 400, 400, fusion.BLUE)

    if fusion.key_down_once(fusion.KEY_a):
        print("Key A pressed")
