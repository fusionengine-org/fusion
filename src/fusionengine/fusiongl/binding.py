import ctypes
from fusionengine.fusiongl.libgl import gl

LINES = 0x0001
QUADS = 0x0007
POINTS = 0x0000

SRC_ALPHA = 0x0302
ONE_MINUS_SRC_ALPHA = 0x0303

BLEND = 0x0BE2
TEXTURE_2D = 0x0DE1
RGBA = 0x1908
UNSIGNED_BYTE = 0x1401

TEXTURE_WRAP_S = 0x2802
TEXTURE_WRAP_T = 0x2803
TEXTURE_MIN_FILTER = 0x2801
TEXTURE_MAG_FILTER = 0x2800
CLAMP_TO_EDGE = 0x812F

NEAREST = 0x2600
REPEAT = 0x2901
LINEAR_MIPMAP_LINEAR = 0x2703
LINEAR = 0x2601

COLOR_BUFFER_BIT = 0x4000
DEPTH_BUFFER_BIT = 0x0100

PROJECTION = 0x1701
MODELVIEW = 0x1700

GL_VERSION = 0x1F02
GL_MAJOR_VERSION = 0x821B
GL_MINOR_VERSION = 0x821C


def Vertex2f(x, y):
    """
    Set a vertex on the screen.

    Args:
        x (float): x coordinate of the vertex
        y (float): y coordinate of the vertex
    """
    gl.glVertex2f(ctypes.c_float(x), ctypes.c_float(y))


def Begin(mode):
    """
    Begin drawing.

    Args:
        mode (int): The mode of drawing
    """
    gl.glBegin(ctypes.c_uint(mode))


def End():
    """
    End drawing.
    """
    gl.glEnd()


def Color4f(r, g, b, a):
    """
    Set the color of the next vertex.

    Args:
        r (float): The red value of the color
        g (float): The green value of the color
        b (float): The blue value of the color
        a (float): The alpha value of the color
    """
    gl.glColor4f(
        ctypes.c_float(r / 255),
        ctypes.c_float(g / 255),
        ctypes.c_float(b / 255),
        ctypes.c_float(a / 255),
    )


def ClearColor(r, g, b, a):
    """
    Set the background color.

    Args:
        r (float): The red value of the color
        g (float): The green value of the color
        b (float): The blue value of the color
        a (float): The alpha value of the color
    """
    gl.glClearColor(
        ctypes.c_float(r / 255),
        ctypes.c_float(g / 255),
        ctypes.c_float(b / 255),
        ctypes.c_float(a / 255),
    )


def LineWidth(width):
    """
    Set the width of the lines.

    Args:
        width (float): The width of the lines
    """
    gl.glLineWidth(ctypes.c_float(width))


def GenTextures(n):
    """
    Generate a texture.

    Args:
        n (int): The amount of textures to generate

    Returns:
        int: The texture id
    """
    texture_id = ctypes.c_uint(0)
    gl.glGenTextures(1, ctypes.byref(texture_id))
    return texture_id.value


def BindTexture(target, texture):
    """
    Bind a texture.

    Args:
        target (int): The target of the texture
        texture (int): The texture id
    """
    gl.glBindTexture(ctypes.c_uint(target), ctypes.c_uint(texture))


def TexImage2D(
    target, level, internalformat, width, height, border, format, type, pixels
):
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
        pixels (ctypes.c_void_p): The pixels of the texture
    """
    gl.glTexImage2D(
        ctypes.c_uint(target),
        ctypes.c_int(level),
        ctypes.c_int(internalformat),
        ctypes.c_int(width),
        ctypes.c_int(height),
        ctypes.c_int(border),
        ctypes.c_uint(format),
        ctypes.c_uint(type),
        pixels,
    )


def GenerateMipmap(target):
    """
    Generate mipmaps.

    Args:
        target (int): The target of the texture
    """
    gl.glGenerateMipmap(ctypes.c_uint(target))


def TexParameteri(target, pname, param):
    """
    Set the parameters of a texture.

    Args:
        target (int): The target of the texture
        pname (int): The name of the parameter
        param (int): The value of the parameter
    """
    gl.glTexParameteri(ctypes.c_uint(target), ctypes.c_uint(pname), ctypes.c_int(param))


def TexParameterf(target, pname, param):
    """
    Set the parameters of a texture.

    Args:
        target (int): The target of the texture
        pname (int): The name of the parameter
        param (float): The value of the parameter
    """
    gl.glTexParameterf(
        ctypes.c_uint(target), ctypes.c_uint(pname), ctypes.c_float(param)
    )


def Clear(buffer_mask):
    """
    Clear the screen.

    Args:
        buffer_mask (int): The target of the clear
    """
    gl.glClear(ctypes.c_uint(buffer_mask))


def ViewPort(x, y, width, height):
    """
    Set viewport.

    Args:
        x (int): x
        y (int): y
        width (int): width
        height (int): height
    """
    gl.glViewport(
        ctypes.c_int(x), ctypes.c_int(y), ctypes.c_int(width), ctypes.c_int(height)
    )


def Ortho(left, right, bottom, top, near, far):
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
    gl.glOrtho(
        ctypes.c_double(left),
        ctypes.c_double(right),
        ctypes.c_double(bottom),
        ctypes.c_double(top),
        ctypes.c_double(near),
        ctypes.c_double(far),
    )


def MatrixMode(mode):
    """
    Set the current matrix mode.

    Args:
        mode (int): The matrix mode to set (e.g., GL_MODELVIEW, GL_PROJECTION).
    """
    gl.glMatrixMode(ctypes.c_uint(mode))


def LoadIdentity():
    """
    Replace the current matrix with the identity matrix.
    """
    gl.glLoadIdentity()


def TexCoord2f(x, y):
    """
    Set the texture coordinates.

    Args:
        x (float): x coordinate of the texture
        y (float): y coordinate of the texture
    """
    gl.glTexCoord2f(ctypes.c_float(x), ctypes.c_float(y))


def Enable(cap):
    """
    Enable a capability.

    Args:
        cap (int): The capability to enable
    """
    gl.glEnable(ctypes.c_uint(cap))


def BlendFunc(sfactor, dfactor):
    """
    Set the pixel blending factors.

    Args:
        sfactor (int): The source blending factor
        dfactor (int): The destination blending factor
    """
    gl.glBlendFunc(ctypes.c_uint(sfactor), ctypes.c_uint(dfactor))


def RasterPos2d(sfactor, dfactor):
    """
    Set the pixel blending factors.

    Args:
        sfactor (float): The source blending factor
        dfactor (float): The destination blending factor
    """
    gl.glRasterPos2d(ctypes.c_double(sfactor), ctypes.c_double(dfactor))


def DrawPixels(width, height, format, type, pixels):
    """
    Draw pixels.

    Args:
        width (int): The width of the pixels
        height (int): The height of the pixels
        format (int): The format of the pixels
        type (int): The type of the pixels
        pixels (ctypes.c_void_p): The pixels
    """
    gl.glDrawPixels(
        ctypes.c_int(width),
        ctypes.c_int(height),
        ctypes.c_uint(format),
        ctypes.c_uint(type),
        pixels,
    )


def TexParameter(target, pname, param):
    """
    Set the parameters of a texture.

    Args:
        target (int): The target of the texture
        pname (int): The name of the parameter
        param (int): The value of the parameter
    """
    gl.glTexParameter(ctypes.c_uint(target), ctypes.c_uint(pname), ctypes.c_int(param))


def Flush():
    """
    Flush all commands.
    """
    gl.glFlush()


def GetString(type) -> bytes | None:
    return ctypes.cast(gl.glGetString(GL_VERSION), ctypes.c_char_p).value


def GetIntegerv(type) -> int:
    integ = ctypes.c_int()
    gl.glGetIntegerv(type, ctypes.byref(integ))
    return int(integ.value)


def GetVersion() -> str:
    major_version = GetIntegerv(GL_MAJOR_VERSION)
    minor_version = GetIntegerv(GL_MINOR_VERSION)

    return str(major_version) + "." + str(minor_version)
