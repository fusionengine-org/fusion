from python import fusionengine as fusion

window = fusion.window.Window("Example: 1", 600, 600)
image = fusion.image.Image(fusion.debug.DEBUGIMAGE, 0, 0, 600, 600)

while window.running():
    image.draw()
