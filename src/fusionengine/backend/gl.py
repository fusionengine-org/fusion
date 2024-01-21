import OpenGL.GL as gl
from OpenGL.constant import FloatConstant, IntConstant

LINES = gl.GL_LINES
QUADS = gl.GL_QUADS
POINTS = gl.GL_POINTS

TEXTURE_2D = gl.GL_TEXTURE_2D
RGBA = gl.GL_RGBA
UNSIGNED_BYTE = gl.GL_UNSIGNED_BYTE

TEXTURE_WRAP_S = gl.GL_TEXTURE_WRAP_S
TEXTURE_WRAP_T = gl.GL_TEXTURE_WRAP_T
TEXTURE_MIN_FILTER = gl.GL_TEXTURE_MIN_FILTER
TEXTURE_MAG_FILTER = gl.GL_TEXTURE_MAG_FILTER

REPEAT = gl.GL_REPEAT
LINEAR_MIPMAP_LINEAR = gl.GL_LINEAR_MIPMAP_LINEAR
LINEAR = gl.GL_LINEAR

COLOR_BUFFER_BIT = gl.GL_COLOR_BUFFER_BIT
DEPTH_BUFFER_BIT = gl.GL_DEPTH_BUFFER_BIT

PROJECTION = gl.GL_PROJECTION
MODELVIEW = gl.GL_MODELVIEW


def Vertex2f(x: float, y: float) -> None:
    """
    Set a vertex on the screen.

    Args:
        x (float): x coordinate of the vertex
        y (float): Y coordinate of the vertex
    """
    gl.glVertex2f(x, y)


def Begin(mode: int) -> None:
    """
    Begin drawing.

    Args:
        mode (int): The mode of drawing
    """
    gl.glBegin(mode)


def End() -> None:
    """
    End drawing.
    """
    gl.glEnd()


def Color4f(r: float, g: float, b: float, a: float) -> None:
    """
    Set the color of the next vertex.

    Args:
        r (float): The red value of the color
        g (float): The green value of the color
        b (float): The blue value of the color
        a (float): The alpha value of the color
    """
    gl.glColor4f(r / 255, g / 255, b / 255, a / 255)


def ClearColor(r: float, g: float, b: float, a: float) -> None:
    """
    Set the background color.

    Args:
        r (float): The red value of the color
        g (float): The green value of the color
        b (float): The blue value of the color
        a (float): The alpha value of the color
    """
    gl.glClearColor(r / 255, g / 255, b / 255, a / 255)


def LineWidth(width: float) -> None:
    """
    Set the width of the lines.

    Args:
        width (float): The width of the lines
    """
    gl.glLineWidth(width)


def GenTextures(n: int) -> int:
    """
    Generate a texture.

    Args:
        n (int): The amount of textures to generate

    Returns:
        int: The texture id
    """
    return gl.glGenTextures(n)


def BindTexture(target: int, texture: int) -> None:
    """
    Bind a texture.

    Args:
        target (int): The target of the texture
        texture (int): The texture id
    """
    gl.glBindTexture(target, texture)


def TexImage2D(
    target: int,
    level: int,
    internalformat: int,
    width: int,
    height: int,
    border: int,
    format: int,
    type: int,
    pixels: bytes,
) -> None:
    """
    Set the image of a texture.

    Args:
        target (int): The target of the texture
        level (int): The level of the texture
        internalformat (int): The internal format of the texture
        width (int): The width of the texture
        height (int): The height of the texture
        border (int): The border of the texture
        format (int): The format of the texture
        type (int): The type of the texture
        pixels (bytes): The pixels of the texture
    """
    gl.glTexImage2D(
        target,
        level,
        internalformat,
        width,
        height,
        border,
        format,
        type,
        pixels,
    )


def GenerateMipmap(target: int) -> None:
    """
    Generate mipmaps.

    Args:
        target (int): The target of the texture
    """
    gl.glGenerateMipmap(target)


def TexParameteri(target: int, pname: int, param: int) -> None:
    """
    Set the parameters of a texture.

    Args:
        target (int): The target of the texture
        pname (int): The name of the parameter
        param (int): The value of the parameter
    """
    gl.glTexParameteri(target, pname, param)


def TexParameterf(target: int, pname: int, param: float) -> None:
    """
    Set the parameters of a texture.

    Args:
        target (int): The target of the texture
        pname (int): The name of the parameter
        param (float): The value of the parameter
    """
    gl.glTexParameterf(target, pname, param)


def Clear(buffer_mask: int) -> None:
    """
    Clear the screen.

    Args:
        target (int): The target of the clear
    """
    gl.glClear(buffer_mask)


def ViewPort(x: int, y: int, width: int, height: int) -> None:
    """
    Set viewpoer

    Args:
        x (int): x
        y (int): y
        width (int): width
        height (int): height
    """

    gl.glViewport(x, y, width, height)


def Ortho(
    left: float, right: float, bottom: float, top: float, near: float, far: float
) -> None:
    """
    Set up an orthographic projection matrix.

    Args:
        left (float): Coordinate of the left clipping plane.
        right (float): Coordinate of the right clipping plane.
        bottom (float): Coordinate of the bottom clipping plane.
        top (float): Coordinate of the top clipping plane.
        near (float): Distance to the near clipping plane.
        far (float): Distance to the far clipping plane.
    """
    gl.glOrtho(left, right, bottom, top, near, far)


def MatrixMode(mode: int) -> None:
    """
    Set the current matrix mode.

    Args:
        mode (int): The matrix mode to set (e.g., GL_MODELVIEW, GL_PROJECTION).
    """
    gl.glMatrixMode(mode)


def LoadIdentity() -> None:
    """
    Replace the current matrix with the identity matrix.
    """
    gl.glLoadIdentity()
