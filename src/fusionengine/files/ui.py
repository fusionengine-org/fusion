import fusionengine.files.window as fe_window
import fusionengine.files.shape as fe_shape

import pygame as pg
import pygame_gui as gui
import os


class Button:
    def __init__(self, rect: fe_shape.Rect, text: str) -> None:
        """Creates a button."""
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
        return self.button.check_pressed()


class Text:
    def __init__(
        self,
        window: fe_window.Window,
        text: str,
        x: int,
        y: int,
        font_path: str,
        font_size: int,
        color: tuple,
    ) -> None:
        """Prints text on the screen."""

        if os.path.exists(font_path):
            font = pg.font.Font(font_path, font_size)
        else:
            font = pg.font.SysFont(font_path, font_size)

        txtsurf = font.render(text, True, color)

        window.window.blit(txtsurf, (x, y))
