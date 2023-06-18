from src.engine.files.imports import *

class DataBodies:
    def __init__(self, window, x, y, w, h):
        self.window = window
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.space = pymunk.Space()
        self.body = pymunk.Body()