from fusionengine.engine.window import Window
from fusionengine.engine.spritesheets import SpriteSheet


class Animation:
    def __init__(
        self, window: Window, images: tuple | SpriteSheet, speed: float
    ) -> None:
        """
        The class to create an Animation.

        Args:
            window: Window
            image (Tuple | Spritesheets): Tuple of Images or a SpriteSheet
            Speed: Int (FPS)
        """
        self.frame = 0
        self.prev_frame = 0
        self.speed = speed

        if isinstance(images, SpriteSheet):
            self.frames = images.frames
        elif isinstance(images, tuple):
            self.frames = images
        else:
            raise ValueError("Images must be a tuple of Images or a SpriteSheet")

        self.window = window

    def play(self) -> None:
        """
        Draw the animation you made before
        """
        if 0 <= int(self.frame) < len(self.frames):
            if not (
                isinstance(self.frame, int)
                or (isinstance(self.frame, float) and self.frame.is_integer())
            ):
                self.frames[int(self.prev_frame)].draw()
            else:
                self.frames[int(self.frame)].draw()

        self.prev_frame = self.frame
        self.frame += self.speed

        if self.frame >= len(self.frames):
            self.frame = 0
