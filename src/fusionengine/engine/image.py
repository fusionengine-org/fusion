from fusionengine.engine.window import Window
from fusionengine.engine.shape import Rect
import fusionengine.backend.gl as gl

import pygame as pg
from PIL import Image as Imager


class Image:
    def __init__(
        self,
        image_path: str | Imager.Image,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> None:
        """
        Opens an image. Can be later rendered with draw method.

        Args:
            image_path (str or Pillow Image): The path to the image | Pillow Image
            x (int): X coordinate of the image
            y (int): Y coordinate of the image
            width (int): Width of the image (scaling allowed)
            height (int): Height of the image (scaling allowed)
        """

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        if isinstance(image_path, str):
            self.image = Imager.open(str(image_path))
        elif isinstance(image_path, Imager.Image):
            self.image = image_path
        else:
            raise ValueError("Invalid image_path type")

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

    def crop(self, left: int, right: int, top: int, bottom: int) -> "Image":
        """
        Crop the image based on the specified boundaries.

        Args:
            left (int): The left boundary of the crop area.
            right (int): The right boundary of the crop area.
            top (int): The top boundary of the crop area.
            bottom (int): The bottom boundary of the crop area.

        Returns:
            Image: A new Image object representing the cropped image.
        """
        return Image(
            self.image.crop((left, right, top, bottom)),
            self.x,
            self.y,
            self.width,
            self.height,
        )

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
