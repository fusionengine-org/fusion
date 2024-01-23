import fusionengine as fusion


class Example(fusion.SceneManager):
    def __init__(self):
        self.window = fusion.Window("Example: 1", 600, 600)
        self.init(self.window)

        self.image = fusion.Image(fusion.DEBUGIMAGE, 0, 0, 600, 600)

        self.add_scene(fusion.Scene("image", self.draw_i))
        self.add_scene(fusion.Scene("rect", self.draw_r))

        self.loop()

    def draw_i(self):
        self.image.draw()

    def draw_r(self):
        fusion.draw_rect(0, 0, 50, 50, fusion.RED)

    def loop(self):
        while self.window.running():
            self.window.set_fps(60)
            self.start()


Example()
