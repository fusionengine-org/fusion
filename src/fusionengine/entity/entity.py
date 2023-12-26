from fusionengine.core.window import Window
from fusionengine.core.image import Image
from fusionengine.core.shape import Rect
from fusionengine.animation.animation import Animation


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

    def load_image(
        self,
        image_path: str,
    ) -> None:
        """Gives the entity an image and laters draws it on the screen."""
        self.main_image = Image(
            self.window, image_path, self.x, self.y, self.width, self.height
        )

    def load_animation(self, window: Window, images: tuple, speed: int):
        self.anim = Animation(window, images, speed)

    def draw_animation(self):
        self.anim.draw()

    def draw_image(self) -> None:
        self.main_image.draw()

    def load_rect(self, color: tuple) -> None:
        """Gives the entity a rectangle and later draws it on the screen."""
        self.main_rect = Rect(self.window, self.x, self.y, self.width, self.height, color)

    def draw_rect(self) -> None:
        self.main_rect.draw()
