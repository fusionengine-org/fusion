import fusionengine as fusion

window = fusion.window.Window("Example: 2", 800, 600)


@window.loop
def loop():
    fusion.draw.set_background_color(window, (fusion.color.VIOLET))
    fusion.draw.draw_rect(window, 100, 100, 400, 400, fusion.color.BLUE)

    if fusion.event.key_down(fusion.keys.KEY_a):
        print("Key A pressed")
