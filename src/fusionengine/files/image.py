from fusionengine.files.imports import *
import fusionengine.files.window as window
import fusionengine.files.shape as shape

class _CustomImage:
    def __init__(self, window: window._CustomRenderer, texture, rect: shape._CustomShape) -> None:
        """A class that creates a new custom image. (Not for the user)"""
        self.window = window
        self.renderer = window.renderer
        self.texture = texture
        self.rect = rect

class Image:
    def open_image(self, window: window._CustomRenderer, image, x: int, y: int, width: int, height: int) -> _CustomImage:
        """Opens an image. Can be later rendered with draw_image."""
        image = sdl2.ext.load_image(image)
        texture = sdl2.SDL_CreateTextureFromSurface(window.renderer, image)
        rect = sdl2.SDL_Rect(x, y, width, height)
        return _CustomImage(window, texture, rect)

    def draw_image(self, image: _CustomImage) -> None:
        """Draws your image (opened with open_image) on the screen."""
        sdl2.SDL_RenderCopy(image.renderer, image.texture, None, image.rect)
