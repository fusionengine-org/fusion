from fusionengine.engine.shape import Rect
from fusionengine.engine.color import Color, WHITE, GRAY
import fusionengine.fusiongl as gl
from fusionengine.engine.debug import DEBUGFONT

import pygame as pg
import os


class Button:
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        font_size: int,
        text: str,
        font: str = DEBUGFONT,
    ) -> None:
        """
        Creates a button. You can get its events using is_pressed() function or you can draw it using draw() function.

        Args:
            x (int): X pos
            y (int): Y pos
            width (int): Width
            height (int): Height
            font_size (int): Font size
            text (str): Text
            font (str, optional): Your Font. Defaults to the default font (DEBUGFONT).
        """
        self.rect_color = GRAY
        self.rect = Rect(x, y, 500, 500, self.rect_color)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.input_text = text
        self.font = font
        self.font_size = font_size

        self.text = Text(text, x, y, font, font_size, WHITE)

    def is_pressed(self) -> bool:
        """
        Returns true if the button is pressed.

        Returns:
            bool: If the button is pressed, returns True
        """
        mouse_x, mouse_y = pg.mouse.get_pos()
        mouse_click = pg.mouse.get_pressed()

        if self.rect.pg_rect.collidepoint(mouse_x, mouse_y) and mouse_click[0] == 1:
            return True
        else:
            return False

    def draw(self) -> None:
        """
        Draws the button.
        """
        self.rect.draw()
        self.text.draw()

    def set_button_color(self, color: Color) -> None:
        """
        Sets the color of the button.

        Args:
            color (Color): The color of the button
        """
        self.rect_color = color
        self.rect.color = color

    def set_text_color(self, color: Color) -> None:
        """
        Sets the color of the button text.

        Args:
            color (Color): The color of the button text
        """
        self.text.set_color(color)


class Text:
    def __init__(
        self,
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
            text (str): The text you want to print
            x (int): X coordinate of the text
            y (int): Y coordinate of the text
            font_path (str): The path to the font file
            font_size (int): The size of the font
            color (tuple): The color of the text
        """

        self.text = text
        self.color = color
        self.x = x
        self.y = y

        if os.path.exists(font_path):
            self.font = pg.font.Font(font_path, font_size)
        else:
            self.font = pg.font.SysFont(font_path, font_size)

        render = self.font.render(self.text, True, self.color.tuple)
        text_surface = pg.image.tostring(render, "RGBA", False)
        self.width, self.height = render.get_size()

        self.texture_id = gl.GenTextures(1)

        gl.BindTexture(gl.TEXTURE_2D, self.texture_id)

        gl.TexImage2D(
            gl.TEXTURE_2D,
            0,
            gl.RGBA,
            self.width,
            self.height,
            0,
            gl.RGBA,
            gl.UNSIGNED_BYTE,
            text_surface,
        )
        gl.TexParameter(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE)
        gl.TexParameter(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE)
        gl.TexParameter(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.NEAREST)
        gl.TexParameter(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.NEAREST)

        gl.BindTexture(gl.TEXTURE_2D, 0)

    def set_color(self, color: Color):
        """
        Sets the color of the text.

        Args:
            color (tuple): The color of the text
        """
        self.color = color

    def draw(self) -> None:
        """
        Draws the loaded font using texture mapping
        """
        gl.BindTexture(gl.TEXTURE_2D, self.texture_id)

        gl.Begin(gl.QUADS)

        gl.Color4f(self.color.r, self.color.g, self.color.b, self.color.a)

        gl.TexCoord2f(0, 0)
        gl.Vertex2f(self.x, self.y)
        gl.TexCoord2f(1, 0)
        gl.Vertex2f(self.x + self.width, self.y)
        gl.TexCoord2f(1, 1)
        gl.Vertex2f(self.x + self.width, self.y + self.height)
        gl.TexCoord2f(0, 1)
        gl.Vertex2f(self.x, self.y + self.height)
        gl.End()

        gl.BindTexture(gl.TEXTURE_2D, 0)
