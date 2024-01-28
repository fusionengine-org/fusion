from fusionengine.engine.window import Window
from fusionengine.engine.spritesheets import SpriteSheet


class Animation:
    def __init__(self, window: Window, images: tuple | SpriteSheet) -> None:
        """
        The class to create a Animation.

        Args:
            window: Window
            image (Tuple | Spritesheets): Tuple of Images or a SpriteSheet
            Speed: Int (FPS)
        """
        self.frame = 0
        if isinstance(images, SpriteSheet):
            self.frames = images.frames
        elif isinstance(images, tuple):
            self.frames = images
        else:
            ValueError("Images must be a tuple of Images or a SpriteSheet")

        self.window = window

    def play(self, speed: float) -> None:
        """
        Draw the animation you made before
        """
        if isinstance(self.frame, int) or (
            isinstance(self.frame, float) and self.frame.is_integer()
        ):
            if 0 <= int(self.frame) < len(self.frames):
                self.frames[int(self.frame)].draw()

        self.frame += speed

        if self.frame >= len(self.frames):
            self.frame = 0
