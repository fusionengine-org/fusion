from fusionengine.engine.window import Window
from fusionengine.engine.shape import Rect

import pygame as pg
import pygame_gui as gui
import os


class Button:
    def __init__(self, rect: Rect, text: str) -> None:
        """
        Creates a button.

        Args:
            rect (Rect): The rect of the button (defines the shape of the button)
            text (str): The text of the button
        """
        self.manager = rect.window.manager
        self.text = text
        self.x = rect.x
        self.y = rect.y
        self.width = rect.width
        self.height = rect.height

        self.button = gui.elements.UIButton(
            relative_rect=rect.rect, text=text, manager=self.manager
        )

    def button_pressed(self) -> bool:
        """
        Returns true if the button is pressed.

        Returns:
            bool: If the button is pressed, returns True
        """
        return self.button.check_pressed()


class Text:
    def __init__(
        self,
        window: Window,
        text: str,
        x: int,
        y: int,
        font_path: str,
        font_size: int,
        color: tuple,
    ) -> None:
        """
        Prints text on the screen.

        Args:
            window (Window): Your window
            text (str): The text you want to print
            x (int): X coordinate of the text
            y (int): Y coordinate of the text
            font_path (str): The path to the font file
            font_size (int): The size of the font
            color (tuple): The color of the text
        """

        if os.path.exists(font_path):
            font = pg.font.Font(font_path, font_size)
        else:
            font = pg.font.SysFont(font_path, font_size)

        txtsurf = font.render(text, True, color)

        window.window.blit(txtsurf, (x, y))
