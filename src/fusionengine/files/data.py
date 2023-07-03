from fusionengine.files.imports import *
import fusionengine.files.window as window

class DataBodies:
    def __init__(self, window: window._CustomRenderer, x: int, y: int, w: int, h: int) -> None:
        self.window = window
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.space = pymunk.Space()
        self.body = pymunk.Body()
        