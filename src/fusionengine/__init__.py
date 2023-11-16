__author__ = "Dimkauzh"
__version__ = "4.0.0"

import sys
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

from fusionengine.files.window import *
from fusionengine.files.image import *
from fusionengine.files.debug import *
from fusionengine.files.color import *
from fusionengine.files.event import *
from fusionengine.files.draw import *
from fusionengine.files.shape import *
from fusionengine.files.body import *
from fusionengine.files.systems import *
from fusionengine.files.storage import *
from fusionengine.files.ui import *
from fusionengine.files.fonts import *
from fusionengine.files.vector import *
from fusionengine.files.math import *
from fusionengine.files.sound import *


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
