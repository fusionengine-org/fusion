__author__ = "Fusion Engine Team"
__version__ = "5.2.0"

import sys
import os
import warnings
import platform

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

# Core
from fusionengine.engine.window import *
from fusionengine.engine.image import *
from fusionengine.engine.draw import *
from fusionengine.engine.shape import *

# Events
from fusionengine.engine.event import *
from fusionengine.engine.keys import *

# Colors
from fusionengine.engine.color import *

# Entity
from fusionengine.engine.entity import *

# Node
from fusionengine.engine.node import *

# Storage
from fusionengine.engine.storage import *

# UI
from fusionengine.engine.ui import *

# Math
from fusionengine.engine.vector import *
from fusionengine.engine.math import *

# Sound
from fusionengine.engine.sound import *

# Scene
from fusionengine.engine.scene import *
from fusionengine.engine.manager import *

# Tools
from fusionengine.engine.debug import *

# Animation
from fusionengine.engine.animation import *
from fusionengine.engine.spritesheets import *

# GL
import fusionengine.fusiongl as gl

import pygame as pg

message = True

if os.environ.get("FUSION_HIDE_PROMPT") is None or not message:
    python_version = sys.version.split()[0]
    print(
        f"Fusion Engine {__version__} (FusionGL {gl.__version__}, Pygame-ce {pg.version.ver}, Python {python_version})"
    )
    print(
        "Welcome to Fusion Engine! Check out our website at https://fusion-engine.tech/"
    )

if platform.system().lower() == "linux":
    warnings.filterwarnings(
        "ignore", message="PyGame seems to be running through X11 on top of wayland"
    )
