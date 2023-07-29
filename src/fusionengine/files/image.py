from fusionengine.files.imports import *
import fusionengine.files.window as window
import fusionengine.files.shape as shape


class _CustomImage:
    def __init__(self, window: window._CustomRenderer, texture, x: int, y: int) -> None:
        """A class that creates a new custom image. (Not for the user)"""
        self.window = window
        self.texture = texture
        self.x = x
        self.y = y


class Image:
    def open_image(
        self,
        window: window._CustomRenderer,
        image,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> _CustomImage:
        """Opens an image. Can be later rendered with draw_image."""
        texture = pg.image.load(image).convert()
        texture = pg.transform.scale(texture, (width, height))
        return _CustomImage(window, texture, x, y)

    def draw_image(self, image: _CustomImage) -> None:
        """Draws your image (opened with open_image) on the screen."""
        image.window.window.blit(image.texture, (image.x, image.y))
