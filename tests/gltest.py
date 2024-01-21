import fusionengine as fusion

window = fusion.Window("GL-Test", 800, 600)


@window.loop
def loop():
    fusion.draw_rect(window, 40, 40, 500, 500, fusion.BLUE)
