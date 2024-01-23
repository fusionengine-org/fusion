import pygame as pg

from fusionengine.engine.window import Window
from fusionengine.engine.color import Color, BLUE
from fusionengine.engine.draw import draw_rect


class Rect:
    def __init__(
        self,
        window: Window,
        x: int,
        y: int,
        width: int,
        height: int,
        color: Color = BLUE,
    ) -> None:
        """
        A class that creates a new rect shape.

        Args:
            window (Window): Your window
            x (int): X coordinate of the rect
            y (int): Y coordinate of the rect
            width (int): Width of the rect
            height (int): Height of the rect
            color (Color): Color of the rect
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window = window
        self.color = color

    def draw(self) -> None:
        """
        Draw the rectangle
        """
        draw_rect(self.window, self.x, self.y, self.width, self.height, self.color)
