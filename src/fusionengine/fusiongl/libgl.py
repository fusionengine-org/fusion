import ctypes
import platform
import os

from ctypes.util import find_library
from warnings import warn

system_platform = platform.system().lower()
if system_platform == "windows":
    library_name = "opengl32"
elif system_platform == "darwin":
    library_name = "OpenGL"
elif system_platform == "linux":
    library_name = "GL"
else:
    if os.environ.get("FUSION_HIDE_GL_PROMPT") is None:
        warn(
            "Your platform could not be resolved. Defaulting to OpenGL as GL. Rever to the documentation to learn about how to remove this warning.",
            category=None,
            stacklevel=1,
        )
    library_name = "GL"

opengl_lib_path = find_library(library_name)
if opengl_lib_path is None:
    raise OSError(f"Could not find the OpenGL library for platform {system_platform}")

gl = ctypes.CDLL(opengl_lib_path)
