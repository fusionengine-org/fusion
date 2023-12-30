from fusionengine.core.window import Window
from fusionengine.core.image import Image
from fusionengine.core.shape import Rect

class Entity:
    def __init__(
        self,
        window: Window,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> None:
        """A class that creates a new entity."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window = window
        self.gravity = 0
        self.frame = 0

    def load_image(
        self,
        image_path: str,
    ) -> None:
        """Gives the entity an image and laters draws it on the screen."""
        self.main_image = Image(
            self.window, image_path, self.x, self.y, self.width, self.height
        )

    def load_animation(self, images: tuple):
        self.images = images

    def draw_animation(self):
        self.images[self.frame].draw()

    def draw_image(self) -> None:
        self.main_image.draw()

    def set_frame(self, frame: int):
        self.frame = frame

    def get_frame(self, frame: int) -> int:
        return frame

    def load_rect(self, color: tuple) -> None:
        """Gives the entity a rectangle and later draws it on the screen."""
        self.main_rect = Rect(self.window, self.x, self.y, self.width, self.height, color)

    def draw_rect(self) -> None:
        self.main_rect.draw()
