__author__ = "Dimkauzh"
__version__ = "4.2.1"

import sys
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

# Core
from fusionengine.core.window import *
from fusionengine.core.image import *
from fusionengine.core.draw import *
from fusionengine.core.shape import *

# Events
from fusionengine.events.event import *
from fusionengine.events.keys import *

# Colors
from fusionengine.colors.color import *
from fusionengine.colors.colortools import *

# Entity
from fusionengine.entity.entity import *

# Physics
from fusionengine.physics.body import *

# Storage
from fusionengine.storage.storage import *

# UI
from fusionengine.ui.ui import *

# Fonts
from fusionengine.fonts.fonts import *

# Math
from fusionengine.math.vector import *
from fusionengine.math.math import *

# Sound
from fusionengine.sound.sound import *
from fusionengine.sound.background import *

# Scene
from fusionengine.scene.scene import *
from fusionengine.scene.manager import *

# Tools
from fusionengine.tools.systems import *
from fusionengine.tools.debug import *

# Animation
from fusionengine.animation.animation import *


import pygame as pg
import pygame_gui as gui

message = True

pg.init()


if os.environ.get("FUSION_HIDE_PROMPT") is None:
    python_version = sys.version.split()[0]
    print(f"Fusion Engine {__version__} (Pygame-ce {pg.version.ver}, Python {python_version})")
    print(
        "Welcome to Fusion Engine! https://github.com/dimkauzh/fusion-engine. Check out our website at https://fusion-engine.tech/"
    )
