from src.engine.files.imports import *

class DataBodies:
    def __init__(self, window, x: int, y: int, w: int, h: int) -> None:
        self.window = window
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.space = pymunk.Space()
        self.body = pymunk.Body()
        