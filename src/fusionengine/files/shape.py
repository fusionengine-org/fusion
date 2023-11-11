import pygame as pg

import fusionengine.files.window as fe_window


class Rect:
    def __init__(
        self, window: fe_window.Window, x: int, y: int, width: int, height: int, color: tuple
    ) -> None:
        """A class that creates a new custom shape. (Not for the user)"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pg.Rect(x, y, width, height)
        self.window = window

    def draw(self) -> None:
        """Creates a new rectangle. Can be later rendered with draw_own_rect."""
        pg.draw.rect(self.window.window, self.color, self.rect)
