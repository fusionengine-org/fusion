from fusionengine.files.imports import *
import fusionengine.files.window as window


class _DataBodies:
    def __init__(self, window: window._CustomRenderer, x: int, y: int, w: int, h: int) -> None:
        """A class that creates a new custom bodies. (Not for the user)"""
        self.window = window
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.space = pymunk.Space()
        self.body = pymunk.Body()
