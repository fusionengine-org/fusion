from engine.files.imports import *

class _CustomShape:
    def __init__(self, x:int, y:int, width:int, height:int, color: tuple) -> None:
        x = x
        y = y
        width = width
        height = height
        color = color
        rect = SDL_Rect(x, y, width, height)

class Shapes:
    def __init__(self) -> None:
        pass
    
    def newRect(self, x:int, y:int, width:int, height:int, color: tuple) -> _CustomShape:
        return _CustomShape(x, y, width, height, color)