from fusionengine.engine.window import Window
from fusionengine.engine.shape import Rect
from fusionengine.engine.color import Color
import fusionengine.backend.gl as gl

import pygame as pg
import os


class Button:
    def __init__(self, rect: Rect, text: str) -> None:
        """
        Creates a button.

        Args:
            rect (Rect): The rect of the button (defines the shape of the button)
            text (str): The text of the button
        """
        print("Not done yet, will be added soon.")

    def button_pressed(self) -> bool:
        """
        Returns true if the button is pressed.

        Returns:
            bool: If the button is pressed, returns True
        """
        return False


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
        Draws the loaded font using texture mapping
        """
        render = self.font.render(self.text, True, self.color.tuple)
        text_surface = pg.image.tostring(render, "RGBA", False)
        width, height = render.get_size()

        texture_id = gl.GenTextures(1)
        gl.BindTexture(gl.TEXTURE_2D, texture_id)
        gl.TexParameter(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.NEAREST)
        gl.TexParameter(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.NEAREST)

        gl.TexImage2D(
            gl.TEXTURE_2D,
            0,
            gl.RGBA,
            width,
            height,
            0,
            gl.RGBA,
            gl.UNSIGNED_BYTE,
            text_surface,
        )

        gl.Enable(gl.TEXTURE_2D)
        gl.Begin(gl.QUADS)
        gl.TexCoord2f(0, 0)
        gl.Vertex2f(self.x, self.y)
        gl.TexCoord2f(1, 0)
        gl.Vertex2f(self.x + width, self.y)
        gl.TexCoord2f(1, 1)
        gl.Vertex2f(self.x + width, self.y + height)
        gl.TexCoord2f(0, 1)
        gl.Vertex2f(self.x, self.y + height)
        gl.End()
