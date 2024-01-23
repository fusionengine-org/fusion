import OpenGL.GL as gl
from OpenGL.constant import FloatConstant, IntConstant

LINES = gl.GL_LINES
QUADS = gl.GL_QUADS
POINTS = gl.GL_POINTS

SRC_ALPHA = gl.GL_SRC_ALPHA
ONE_MINUS_SRC_ALPHA = gl.GL_ONE_MINUS_SRC_ALPHA

BLEND = gl.GL_BLEND
TEXTURE_2D = gl.GL_TEXTURE_2D
RGBA = gl.GL_RGBA
UNSIGNED_BYTE = gl.GL_UNSIGNED_BYTE

TEXTURE_WRAP_S = gl.GL_TEXTURE_WRAP_S
TEXTURE_WRAP_T = gl.GL_TEXTURE_WRAP_T
TEXTURE_MIN_FILTER = gl.GL_TEXTURE_MIN_FILTER
TEXTURE_MAG_FILTER = gl.GL_TEXTURE_MAG_FILTER
CLAMP_TO_EDGE = gl.GL_CLAMP_TO_EDGE

NEAREST = gl.GL_NEAREST
REPEAT = gl.GL_REPEAT
LINEAR_MIPMAP_LINEAR = gl.GL_LINEAR_MIPMAP_LINEAR
LINEAR = gl.GL_LINEAR

COLOR_BUFFER_BIT = gl.GL_COLOR_BUFFER_BIT
DEPTH_BUFFER_BIT = gl.GL_DEPTH_BUFFER_BIT

PROJECTION = gl.GL_PROJECTION
MODELVIEW = gl.GL_MODELVIEW


def Vertex2f(x, y):
    """
    Set a vertex on the screen.

    Args:
        x: x coordinate of the vertex
        y: Y coordinate of the vertex
    """
    gl.glVertex2f(x, y)


def Begin(mode):
    """
    Begin drawing.

    Args:
        mode: The mode of drawing
    """
    gl.glBegin(mode)


def End():
    """
    End drawing.
    """
    gl.glEnd()


def Color4f(r, g, b, a):
    """
    Set the color of the next vertex.

    Args:
        r: The red value of the color
        g: The green value of the color
        b: The blue value of the color
        a: The alpha value of the color
    """
    gl.glColor4f(r / 255, g / 255, b / 255, a / 255)


def ClearColor(r, g, b, a):
    """
    Set the background color.

    Args:
        r: The red value of the color
        g: The green value of the color
        b: The blue value of the color
        a: The alpha value of the color
    """
    gl.glClearColor(r / 255, g / 255, b / 255, a / 255)


def LineWidth(width):
    """
    Set the width of the lines.

    Args:
        width: The width of the lines
    """
    gl.glLineWidth(width)


def GenTextures(n):
    """
    Generate a texture.

    Args:
        n: The amount of textures to generate

    Returns:
        int: The texture id
    """
    return gl.glGenTextures(n)


def BindTexture(target, texture):
    """
    Bind a texture.

    Args:
        target: The target of the texture
        texture: The texture id
    """
    gl.glBindTexture(target, texture)


def TexImage2D(
    target, level, internalformat, width, height, border, format, type, pixels
):
    """
    Set the image of a texture.

    Args:
        target: The target of the texture
        level: The level of the texture
        internalformat: The internal format of the texture
        width: The width of the texture
        height: The height of the texture
        border: The border of the texture
        format: The format of the texture
        type: The type of the texture
        pixels: The pixels of the texture
    """
    gl.glTexImage2D(
        target, level, internalformat, width, height, border, format, type, pixels
    )


def GenerateMipmap(target):
    """
    Generate mipmaps.

    Args:
        target: The target of the texture
    """
    gl.glGenerateMipmap(target)


def TexParameteri(target, pname, param):
    """
    Set the parameters of a texture.

    Args:
        target: The target of the texture
        pname: The name of the parameter
        param: The value of the parameter
    """
    gl.glTexParameteri(target, pname, param)


def TexParameterf(target, pname, param):
    """
    Set the parameters of a texture.

    Args:
        target: The target of the texture
        pname: The name of the parameter
        param: The value of the parameter
    """
    gl.glTexParameterf(target, pname, param)


def Clear(buffer_mask):
    """
    Clear the screen.

    Args:
        target: The target of the clear
    """
    gl.glClear(buffer_mask)


def ViewPort(x, y, width, height):
    """
    Set viewport.

    Args:
        x: x
        y: y
        width: width
        height: height
    """
    gl.glViewport(x, y, width, height)


def Ortho(left, right, bottom, top, near, far):
    """
    Set up an orthographic projection matrix.

    Args:
        left: Coordinate of the left clipping plane.
        right: Coordinate of the right clipping plane.
        bottom: Coordinate of the bottom clipping plane.
        top: Coordinate of the top clipping plane.
        near: Distance to the near clipping plane.
        far: Distance to the far clipping plane.
    """
    gl.glOrtho(left, right, bottom, top, near, far)


def MatrixMode(mode):
    """
    Set the current matrix mode.

    Args:
        mode: The matrix mode to set (e.g., GL_MODELVIEW, GL_PROJECTION).
    """
    gl.glMatrixMode(mode)


def LoadIdentity():
    """
    Replace the current matrix with the identity matrix.
    """
    gl.glLoadIdentity()


def TexCoord2f(x, y):
    """
    Set the texture coordinates.

    Args:
        x: x coordinate of the texture
        y: y coordinate of the texture
    """
    gl.glTexCoord2f(x, y)


def Enable(cap):
    """
    Enable a capability.

    Args:
        cap: The capability to enable
    """
    gl.glEnable(cap)


def BlendFunc(sfactor, dfactor):
    """
    Set the pixel blending factors.

    Args:
        sfactor: The source blending factor
        dfactor: The destination blending factor
    """
    gl.glBlendFunc(sfactor, dfactor)


def RasterPos2d(sfactor, dfactor):
    """
    Set the pixel blending factors.

    Args:
        sfactor: The source blending factor
        dfactor: The destination blending factor
    """
    gl.glRasterPos2d(sfactor, dfactor)


def DrawPixels(width, height, format, type, pixels):
    """
    Draw pixels.

    Args:
        width: The width of the pixels
        height: The height of the pixels
        format: The format of the pixels
        type: The type of the pixels
        pixels: The pixels
    """
    gl.glDrawPixels(width, height, format, type, pixels)


def TexParameter(target, pname, param):
    """
    Set the parameters of a texture.

    Args:
        target: The target of the texture
        pname: The name of the parameter
        param: The value of the parameter
    """
    gl.glTexParameter(target, pname, param)


def Flush():
    """
    Flush all commands.
    """
    gl.glFlush()
