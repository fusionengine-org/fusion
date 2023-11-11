import fusionengine as fusion

window = fusion.window.Window("Example: 1", 600, 600)
image = fusion.image.Image(window, fusion.debug.DEBUGIMAGE, 0, 0, 600, 600)


@window.loop
def loop():
    window.set_fps(60)
    image.draw()
