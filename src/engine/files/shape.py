from src.engine.files.imports import *

class _CustomShape:
    def __init__(self, x, y, width, height, color):
        x = x
        y = y
        width = width
        height = height
        color = color
        rect = SDL_Rect(x, y, width, height)

class Shapes:
    def __init__(self):
        pass
    
    def newRect(self, x, y, width, height, color):
        return _CustomShape(x, y, width, height, color)