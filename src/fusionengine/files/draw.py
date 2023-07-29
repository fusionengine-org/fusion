import fusionengine.files.systems as sysconfig
import fusionengine.files.window as window

from fusionengine.files.imports import *
import fusionengine.files.shape as shape


class Draw:
    def __init__(self) -> None:
        self.rendereroptions = sysconfig.RendererOptions()

    def draw_line(
        self, window: window._CustomRenderer, x1: int, y1: int, x2: int, y2: int, color: tuple
    ) -> None:
        """Draws a line on the screen."""
        pg.draw.line(window.window, color, (x1, y1), (x2, y2))

    def draw_line_rect(
        self, window: window._CustomRenderer, x: int, y: int, width: int, height: int, color: tuple
    ) -> None:
        """Draws a rectangle that exists of lines on the screen."""
        rdr = window.window
        pg.draw.line(rdr, color, (x, y), (x + width, y))
        pg.draw.line(rdr, color, (x, y + height), (x + width, y + height))
        pg.draw.line(rdr, color, (x, y), (x, y + height))
        pg.draw.line(rdr, color, (x + width, y), (x + width, y + height))

    def draw_rect(
        self, window: window._CustomRenderer, x: int, y: int, width: int, height: int, color: tuple
    ) -> None:
        """Draws a rectangle on the screen."""
        rect = pg.Rect(x, y, width, height)
        pg.draw.rect(window.window, color, rect)

    def draw_own_rect(self, window: window._CustomRenderer, rect: shape._CustomShape) -> None:
        """Draws your rectangle on the screen."""
        pg.draw.rect(window.window, rect.color, rect.rect)

    def set_background_color(self, window: window._CustomRenderer, color: tuple) -> None:
        """Sets the background color of the screen."""
        window.window.fill(color)
