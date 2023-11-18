import fusionengine as fusion

window = fusion.Window("Example: 1", 600, 600)
image = fusion.Image(window, fusion.DEBUGIMAGE, 0, 0, 600, 600)

manager = fusion.SceneManager(window)


def draw_i():
    image.draw()


def draw_r():
    fusion.draw_rect(window, 0, 0, 50, 50, fusion.RED)


manager.add_scene(fusion.Scene("image", draw_i))
manager.add_scene(fusion.Scene("rect", draw_r))


@window.loop
def loop():
    window.set_fps(60)
    manager.start()
