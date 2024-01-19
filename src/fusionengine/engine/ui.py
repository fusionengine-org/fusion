from fusionengine.engine.window import Window
from fusionengine.engine.shape import Rect
from fusionengine.engine.color import Color

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
        color: Color,
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

        self.text = text
        self.color = color
        self.window = window.window
        self.x = x
        self.y = y

        if os.path.exists(font_path):
            self.font = pg.font.Font(font_path, font_size)
        else:
            self.font = pg.font.SysFont(font_path, font_size)

    def draw(self) -> None:
        """
        Draws the loaded font
        """
        txtsurf = self.font.render(self.text, True, self.color.tuple)
        self.window.blit(txtsurf, (self.x, self.y))
