__author__ = "Dimkauzh"
__version__ = "4.3.0"

import sys
import os

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
from fusionengine.engine.colortools import *

# Entity
from fusionengine.engine.entity import *

# Storage
from fusionengine.engine.storage import *

# UI
from fusionengine.engine.ui import *

# Fonts
from fusionengine.engine.fonts import *

# Math
from fusionengine.engine.vector import *
from fusionengine.engine.math import *

# Sound
from fusionengine.engine.sound import *
from fusionengine.engine.background import *

# Scene
from fusionengine.engine.scene import *
from fusionengine.engine.manager import *

# Tools
from fusionengine.engine.debug import *

# Animation
from fusionengine.engine.animation import *


import pygame as pg
import pygame_gui as gui

message = True


if os.environ.get("FUSION_HIDE_PROMPT") is None:
    python_version = sys.version.split()[0]
    print(
        f"Fusion Engine {__version__} (Pygame-ce {pg.version.ver}, Python {python_version})"
    )
    print(
        "Welcome to Fusion Engine! Check out our website at https://fusion-engine.tech/"
    )
