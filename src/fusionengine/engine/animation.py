from fusionengine.engine.window import Window


class Animation:
    def __init__(self, window: Window, images: tuple, speed: int) -> None:
        """
        The class to create a Animation.

        Args:
            window: Window
            image: tuple of Images
            Speed: Int (FPS)
        """
        self.frame = 0
        self.anim = images

        self.speed = speed
        self.window = window

    def draw(self) -> None:
        """
        Draw the animation you made before
        """
        self.window.set_fps(self.speed)

        if self.frame >= len(self.anim):
            self.frame = 0

        image = self.anim[self.frame]

        image.draw()

        self.frame += 1
