import fusionengine.files.window as window
import pygame as pg


class Image:
    def __init__(
        self,
        window: window.Window,
        image_path,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> None:
        """Opens an image. Can be later rendered with draw_image."""
        image = pg.image.load(image_path).convert_alpha()
        self.texture = pg.transform.scale(image, (width, height))
        self.x = x
        self.y = y
        self.window = window
        self.width = width
        self.height = height

    def draw(self) -> None:
        """Draws your image (opened with open_image) on the screen."""
        self.window.window.blit(self.texture, (self.x, self.y))


def draw_image_file(
    self, window: window.Window, path: str, x: int, y: int, width: int, height: int
):
    """Draw image directly from provided path."""
    texture = pg.image.load(path)
    texture = pg.transform.scale(texture, (width, height))
    window.window.blit(texture, (x, y))
