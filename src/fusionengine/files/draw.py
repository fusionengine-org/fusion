import fusionengine.files.window as window
import pygame as pg


def draw_line(window: window.Window, x1: int, y1: int, x2: int, y2: int, color: tuple) -> None:
    """Draws a line on the screen."""
    pg.draw.line(window.window, color, (x1, y1), (x2, y2))


def draw_line_rect(
    window: window.Window,
    x: int,
    y: int,
    width: int,
    height: int,
    color: tuple,
) -> None:
    """Draws a rectangle that exists of lines on the screen."""
    rdr = window.window
    pg.draw.line(rdr, color, (x, y), (x + width, y))
    pg.draw.line(rdr, color, (x, y + height), (x + width, y + height))
    pg.draw.line(rdr, color, (x, y), (x, y + height))
    pg.draw.line(rdr, color, (x + width, y), (x + width, y + height))


def draw_rect(
    window: window.Window,
    x: int,
    y: int,
    width: int,
    height: int,
    color: tuple,
) -> None:
    """Draws a rectangle on the screen."""
    s = pg.Surface((width, height), pg.SRCALPHA)
    s.fill((color[0], color[1], color[2], color[3]))
    window.window.blit(s, (x, y))


def set_background_color(window: window.Window, color: tuple) -> None:
    """Sets the background color of the screen."""
    s = pg.Surface((window.width, window.height), pg.SRCALPHA)
    s.fill(color)
    window.window.blit(s, (0, 0))


def draw_arbitrary_polygon_outline(
    window: window.Window,
    corners: tuple[tuple[int, int]],
    color: tuple[int, int, int, int],
) -> None:
    """Draw an arbitrary polygon outline.
    WARNING: This will lag the game more and more as the number of corners increase, as this is an O(n)/call function.
    """
    for i, (x1, y1) in enumerate(corners[:-1]):  # need to exclude last corner for IndexError
        x2, y2 = corners[i + 1]  # tuple unpacking
        draw_line(window, x1, y1, x2, y2, color)


def set_pixel(window: window.Window, x, y, color):
    window.window.set_at((x, y), color)
