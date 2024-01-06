import pygame as pg

from fusionengine.engine.window import Window


class Rect:
    def __init__(
        self,
        window: Window,
        x: int,
        y: int,
        width: int,
        height: int,
        color: tuple[int, int, int, int],
    ) -> None:
        """
        A class that creates a new rect shape.

        Args:
            window (Window): Your window
            x (int): X coordinate of the rect
            y (int): Y coordinate of the rect
            width (int): Width of the rect
            height (int): Height of the rect
            color (tuple[int, int, int, int]): Color of the rect
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pg.Rect(x, y, width, height)
        self.window = window

    def draw(self) -> None:
        """
        Draw the rectangle
        """
        pg.draw.rect(self.window.window, self.color, self.rect)
