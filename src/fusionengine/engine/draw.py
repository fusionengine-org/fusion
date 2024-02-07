from fusionengine.engine.window import Window
from fusionengine.engine.color import Color
import fusionengine.fusiongl as gl

import pygame as pg


def draw_line(x1: int, y1: int, x2: int, y2: int, color: Color) -> None:
    """
    Draw a line on the screen

    Args:
        x1 (int): The x position of the first point
        y1 (int): The y position of the first point
        x2 (int): The x position of the second point
        y2 (int): The y position of the second point
        color (Color): The color of the line
    """

    gl.LineWidth(1)

    gl.Begin(gl.LINES)

    gl.Color4f(color.r, color.g, color.b, color.a)
    gl.Vertex2f(x1, y1)
    gl.Vertex2f(x2, y2)

    gl.End()


def draw_line_rect(
    x: int,
    y: int,
    width: int,
    height: int,
    color: Color,
) -> None:
    """
    Draws a rectangle that exists of lines on the screen.

    Args:
        x (int): x coordinate of the rectangle
        y (int): Y coordinate of the rectangle
        width (int): Width of the rectangle
        height (int): Height of the rectangle
        color (Color): Color of the rectangle
    """
    draw_line(x, y, x + width, y, color)
    draw_line(x, y + height, x + width, y + height, color)
    draw_line(x, y, x, y + height, color)
    draw_line(x + width, y, x + width, y + height, color)


def draw_rect(
    x: int,
    y: int,
    width: int,
    height: int,
    color: Color,
) -> None:
    """
    Draws a rectangle on the screen.

    Args:
        x (int): x coordinate of the rectangle
        y (int): Y coordinate of the rectangle
        width (int): Width of the rectangle
        height (int): Height of the rectangle
        color (Color): Color of the rectangle
    """

    gl.Begin(gl.QUADS)

    gl.Color4f(color.r, color.g, color.b, color.a)
    gl.Vertex2f(x, y)
    gl.Vertex2f(x + width, y)
    gl.Vertex2f(x + width, y + height)
    gl.Vertex2f(x, y + height)

    gl.End()


def set_background_color(color: Color) -> None:
    """
    Sets the background color of the screen.

    Args:
        color (Color): The color of the background
    """
    gl.ClearColor(color.r, color.g, color.b, color.a)


def draw_arbitrary_polygon_outline(
    corners: tuple[tuple[int, int]], color: Color
) -> None:
    """
    Draw an arbitrary polygon outline.
    WARNING: This will lag the game more and more as the number of corners increase, as this is an O(n)/call function.

    Args:
        corners (tuple[tuple[int, int]]): The corners of the polygon
        color (Color): The color of the polygon
    """

    for i, (x1, y1) in enumerate(corners[:-1]):
        x2, y2 = corners[i + 1]
        draw_line(x1, y1, x2, y2, color)


def set_pixel(x: int, y: int, color: Color) -> None:
    """
    Set a specific pixel on the window

    Args:
        x (int): The x coordinate of the pixel
        y (int): The y coordinate of the pixel
        color (Color): The color of the pixel
    """
    gl.Begin(gl.POINTS)

    gl.Color4f(color.r, color.g, color.b, color.a)
    gl.Vertex2f(x, y)

    gl.End()
