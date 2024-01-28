from fusionengine.engine.window import Window
from fusionengine.engine.shape import Rect
import fusionengine.backend.gl as gl

import pygame as pg
from PIL import Image as Imager


class Image:
    def __init__(
        self,
        image_path: str,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> None:
        """
        Opens an image. Can be later rendered with draw_image.

        Args:
            image_path (str): The path to the image
            x (int): X coordinate of the image
            y (int): Y coordinate of the image
            width (int): Width of the image (scaling allowed)
            height (int): Height of the image (scaling allowed)
        """

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.image = Imager.open(image_path)
        image_data = self.image.tobytes("raw", "RGBA", 0, -1)

        self.texture = gl.GenTextures(1)
        gl.BindTexture(gl.TEXTURE_2D, self.texture)
        gl.TexImage2D(
            gl.TEXTURE_2D,
            0,
            gl.RGBA,
            self.image.width,
            self.image.height,
            0,
            gl.RGBA,
            gl.UNSIGNED_BYTE,
            image_data,
        )

        gl.TexParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE)
        gl.TexParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE)
        gl.TexParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR)
        gl.TexParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR)

    def draw(self) -> None:
        """
        Draws your image on the screen.
        """
        gl.BindTexture(gl.TEXTURE_2D, self.texture)
        gl.Begin(gl.QUADS)

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


def draw_image(path: str, x: int, y: int, width: int, height: int):
    """
    Draws a image directly from provided path.

    Args:
        image_path (str): The path to the image
        x (int): X coordinate of the image
        y (int): Y coordinate of the image
        width (int): Width of the image (scaling allowed)
        height (int): Height of the image (scaling allowed)
    """
    Image(path, x, y, width, height).draw()
