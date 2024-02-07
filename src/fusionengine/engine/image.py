import fusionengine.fusiongl as gl

import pygame as pg


class Image:
    def __init__(
        self,
        image_path: str | pg.Surface,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> None:
        """
        Opens an image. Can be later rendered with draw method.

        Args:
            image_path (str or Pygame Surface): The path to the image | Pygame Surface
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
            self.image = pg.image.load(image_path)
        elif isinstance(image_path, pg.Surface):
            self.image = image_path
        else:
            raise ValueError("Invalid image_path type")

        self.texture = gl.GenTextures(1)
        gl.BindTexture(gl.TEXTURE_2D, self.texture)
        gl.TexImage2D(
            gl.TEXTURE_2D,
            0,
            gl.RGBA,
            self.image.get_width(),
            self.image.get_height(),
            0,
            gl.RGBA,
            gl.UNSIGNED_BYTE,
            pg.image.tostring(self.image, "RGBA"),
        )

        gl.TexParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE)
        gl.TexParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE)
        gl.TexParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR)
        gl.TexParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR)

    def get_image_size(self):
        """
        Returns the size of the image itself (not the set size).

        Returns:
            tuple: (width, height)
        """
        return self.image.get_width(), self.image.get_height()

    def crop(self, x: int, y: int, width: int, height: int) -> "Image":
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
        cropped_surface = self.image.subsurface((x, y, width, height))
        return Image(cropped_surface, self.x, self.y, self.width, self.height)

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
