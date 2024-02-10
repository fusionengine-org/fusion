import fusionengine as fusion

window = fusion.Window("Example: 1", 600, 600)
image1 = fusion.Image(fusion.DEBUGIMAGE, 0, 0, 600, 600)
image2 = fusion.Image(fusion.DEBUGIMAGE, 0, 0, 400, 400)

anim = fusion.Animation(window, (image1, image2), 3)


@window.loop
def loop():
    anim.play()
