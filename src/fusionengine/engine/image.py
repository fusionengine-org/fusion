from fusionengine.engine.window import Window
import pygame as pg


class Image:
    def __init__(
        self,
        window: Window,
        image_path: str,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> None:
        """
        Opens an image. Can be later rendered with draw_image.

        Args:
            window (Window): Your window
            image_path (str): The path to the image
            x (int): X coordinate of the image
            y (int): Y coordinate of the image
            width (int): Width of the image (scaling allowed)
            height (int): Height of the image (scaling allowed)
        """
        image = pg.image.load(image_path).convert_alpha()

        self.texture = pg.transform.scale(image, (width, height))
        self.x = x
        self.y = y
        self.window = window
        self.width = width
        self.height = height

    def draw(self) -> None:
        """
        Draws your image on the screen.
        """
        self.window.window.blit(self.texture, (self.x, self.y))


def draw_image_file(window: Window, path: str, x: int, y: int, width: int, height: int):
    """
    Draws a image directly from provided path.

    Args:
        window (Window): Your window
        image_path (str): The path to the image
        x (int): X coordinate of the image
        y (int): Y coordinate of the image
        width (int): Width of the image (scaling allowed)
        height (int): Height of the image (scaling allowed)
    """
    texture = pg.image.load(path)
    texture = pg.transform.scale(texture, (width, height))
    window.window.blit(texture, (x, y))
