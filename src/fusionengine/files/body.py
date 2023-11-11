import fusionengine.files.window as window
import fusionengine.files.image as image
import fusionengine.files.shape as shape


class Entity:
    def __init__(
        self,
        window: window.Window,
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
        self.main_image = image.Image(
            self.window, image_path, self.x, self.y, self.width, self.height
        )

    def draw_image(self) -> None:
        self.main_image.draw()

    def load_rect(self, color: tuple) -> None:
        """Gives the entity a rectangle and later draws it on the screen."""
        self.main_rect = shape.Rect(self.window, self.x, self.y, self.width, self.height, color)

    def draw_rect(self) -> None:
        self.main_rect.draw()
