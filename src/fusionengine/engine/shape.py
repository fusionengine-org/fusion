from fusionengine.engine.color import Color, BLUE
from fusionengine.engine.draw import draw_rect

import pygame as pg


class Rect:
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        color: Color = BLUE,
    ) -> None:
        """
        A class that creates a new rect shape.

        Args:
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
        self.color = color

        self.pg_rect = pg.Rect(self.x, self.y, self.width, self.height)

    def draw(self) -> None:
        """
        Draw the rectangle
        """
        draw_rect(self.x, self.y, self.width, self.height, self.color)
