from fusionengine.core.window import Window

class Animation:
    def __init__(self, window: Window, images: tuple, speed: int) -> None:
        self.frame = 0
        self.anim = images
        
        self.speed = speed
        self.window = window

    def draw(self):
        #default_fps = self.window.get_fps()
        self.window.set_fps(self.speed)
        
        if self.frame >= len(self.anim):
            self.frame = 0

        image = self.anim[self.frame]

        image.draw()

        self.frame += 1
        #self.window.set_fps(default_fps)

