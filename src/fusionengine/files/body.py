import fusionengine.files.window as window
from fusionengine.files.enums import BodyType
from fusionengine.files.imports import *
import fusionengine.files.image as image_fe
import fusionengine.files.draw as draw_fe

class _CustomBody:
    def __init__(
            self, window: window._CustomRenderer, x: int, y: int, w: int, h: int
        ) -> None:
            """A class that creates a new custom bodies. (Not for the user)"""
            self.window = window
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.space = pymunk.Space()
            self.body = pymunk.Body()

class _RigidBody:
    def __init__(
        self, window: window._CustomRenderer, x: int, y: int, width: int, height: int
    ) -> None:
        """A class that creates a new rigid body. (Not for the user)"""
        self._body = _CustomBody(window, x, y, width, height)
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.body = self._body.body
        self.space = self._body.space


class _StaticBody:
    def __init__(
        self, window: window._CustomRenderer, x: int, y: int, width: int, height: int
    ) -> None:
        """A class that creates a new static body. (Not for the user)"""
        self._body = _CustomBody(window, x, y, width, height)
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.body = self._body.body
        self.space = self._body.space


class Entity:
    def __init__(
        self,
        window: window._CustomRenderer,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> None:
        """A class that creates a new entity."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window = window
        self.gravity = 0
        self.image_fe = image_fe.Image()
        self.draw_fe = draw_fe.Draw()


    def image(
        self,
        window: window._CustomRenderer,
        image_path: str,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> None:
        """Gives the entity an image and laters draws it on the screen."""
        drawimage = self.image_fe.open_image(window, image_path, x, y, width, height)
        self.image_fe.draw_image(drawimage)
        self.image_path = image_path
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw_rect(self, window: window._CustomRenderer, color: tuple) -> None:
        """Gives the entity a rectangle and later draws it on the screen."""
        self.draw_fe.draw_rect(window, self.x, self.y, self.width, self.height, color)

