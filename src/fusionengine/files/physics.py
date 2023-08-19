from fusionengine.files import window
from fusionengine.files.imports import *


class _CustomBody:
    def __init__(self, window: window._CustomRenderer, x: int, y: int, w: int, h: int) -> None:
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
