import fusionengine as fusion

window = fusion.Window("Example: 1", 600, 600)
image = fusion.Image(fusion.DEBUGIMAGE, 0, 0, 600, 600)


@window.loop
def loop():
    image.draw()
