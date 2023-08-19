import fusionengine.files.window as window
from fusionengine.files.enums import BodyType
from fusionengine.files.imports import *
import fusionengine.files.image as image_fe
import fusionengine.files.draw as draw_fe


class Entity:
    def __init__(
        self,
        window: window._CustomRenderer,
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
        self.image_fe = image_fe.Image()
        self.draw_fe = draw_fe.Draw()

    def image(
        self,
        image_path: str,
    ) -> None:
        """Gives the entity an image and laters draws it on the screen."""
        drawimage = self.image_fe.open_image(
            self.window, image_path, self.x, self.y, self.width, self.height
        )
        self.image_fe.draw_image(drawimage)

    def draw_rect(self, color: tuple) -> None:
        """Gives the entity a rectangle and later draws it on the screen."""
        self.draw_fe.draw_rect(self.window, self.x, self.y, self.width, self.height, color)
