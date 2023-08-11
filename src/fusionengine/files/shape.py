from fusionengine.files.imports import *


class _CustomShape:
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple) -> None:
        """A class that creates a new custom shape. (Not for the user)"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pg.Rect(x, y, width, height)


class Shapes:
    def __init__(self) -> None:
        pass

    def new_rect(
        self, x: int, y: int, width: int, height: int, color: tuple
    ) -> _CustomShape:
        """Creates a new rectangle. Can be later rendered with draw_own_rect."""
        return _CustomShape(x, y, width, height, color)

    def new_rect_button(self, x, y, width, height):
        """Creates a new rectangle button. Can be later rendered with draw_own_rect."""
        return _CustomShape(x, y, width, height, ())
