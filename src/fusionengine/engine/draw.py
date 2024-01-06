from fusionengine.engine.window import Window
import pygame as pg


def draw_line(window: Window, x1: int, y1: int, x2: int, y2: int, color: tuple) -> None:
    """
    Draw a line on the screen

    Args:
        window (Window): Your window
        x1 (int): The x position of the first point
        y1 (int): The y position of the first point
        x2 (int): The x position of the second point
        y2 (int): The y position of the second point
        color (tuple): The color of the line
    """
    pg.draw.line(window.window, color, (x1, y1), (x2, y2))


def draw_line_rect(
    window: Window,
    x: int,
    y: int,
    width: int,
    height: int,
    color: tuple[int, int, int, int],
) -> None:
    """
    Draws a rectangle that exists of lines on the screen.

    Args:
        window (Window): Your window
        x (int): x coordinate of the rectangle
        y (int): Y coordinate of the rectangle
        width (int): Width of the rectangle
        height (int): Height of the rectangle
        color (tuple[int, int, int, int]): Color of the rectangle
    """
    rdr = window.window
    pg.draw.line(rdr, color, (x, y), (x + width, y))
    pg.draw.line(rdr, color, (x, y + height), (x + width, y + height))
    pg.draw.line(rdr, color, (x, y), (x, y + height))
    pg.draw.line(rdr, color, (x + width, y), (x + width, y + height))


def draw_rect(
    window: Window,
    x: int,
    y: int,
    width: int,
    height: int,
    color: tuple[int, int, int, int],
) -> None:
    """
    Draws a rectangle on the screen.

    Args:
        window (Window): Your window
        x (int): x coordinate of the rectangle
        y (int): Y coordinate of the rectangle
        width (int): Width of the rectangle
        height (int): Height of the rectangle
        color (tuple[int, int, int, int]): Color of the rectangle
    """

    s = pg.Surface((width, height), pg.SRCALPHA)
    s.fill((color[0], color[1], color[2], color[3]))
    window.window.blit(s, (x, y))


def set_background_color(window: Window, color: tuple[int, int, int, int]) -> None:
    """
    Sets the background color of the screen.

    Args:
        window (Window): Your window
        color (tuple[int, int, int, int]): The color of the background
    """
    s = pg.Surface((window.width, window.height), pg.SRCALPHA)
    s.fill(color)
    window.window.blit(s, (0, 0))


def draw_arbitrary_polygon_outline(
    window: Window, corners: tuple[tuple[int, int]], color: tuple[int, int, int, int]
) -> None:
    """
    Draw an arbitrary polygon outline.
    WARNING: This will lag the game more and more as the number of corners increase, as this is an O(n)/call function.

    Args:
        window (Window): Your window
        corners (tuple[tuple[int, int]]): The corners of the polygon
        color (tuple[int, int, int, int]): The color of the polygon
    """

    for i, (x1, y1) in enumerate(corners[:-1]):
        x2, y2 = corners[i + 1]
        draw_line(window, x1, y1, x2, y2, color)


def set_pixel(window: Window, x: int, y: int, color: tuple[int, int, int, int]) -> None:
    """
    Set a specific pixel on the window

    Args:
        window (Window): Your window
        x (int): The x coordinate of the pixel
        y (int): The y coordinate of the pixel
        color (tuple[int, int, int, int]): The color of the pixel
    """
    window.window.set_at((x, y), color)
