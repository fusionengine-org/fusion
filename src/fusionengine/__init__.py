__author__ = "Dimkauzh"
__version__ = "3.0.8"

import sys
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import fusionengine.files.window as fe_window
import fusionengine.files.image as fe_image
import fusionengine.files.debug as fe_debug
import fusionengine.files.color as fe_color
import fusionengine.files.event as fe_event
import fusionengine.files.draw as fe_draw
import fusionengine.files.shape as fe_shape
import fusionengine.files.body as fe_body
import fusionengine.files.systems as fe_sysconfig
import fusionengine.files.ui as fe_ui
import fusionengine.files.fonts as fe_fonts
import fusionengine.files.vector as fe_vector
import fusionengine.files.math as fe_math
import fusionengine.files.sound as fe_sound

import pygame as pg

message = True

pg.init()

window = fe_window
color = fe_color.Colors()
colortools = fe_color.ColorTools()
event = fe_event.Event()
keys = fe_event.Keys()
draw = fe_draw.Draw()
image = fe_image
body = fe_body
system = fe_sysconfig.System()
shape = fe_shape
ui = fe_ui
fonts = fe_fonts.Fonts()
debug = fe_debug.DebugFiles()
vector = fe_vector
math = fe_math.Math()
sound = fe_sound

if os.environ.get("FUSION_HIDE_PROMPT") is None:
    python_version = sys.version.split()[0]
    print(f"Fusion Engine {__version__} (Pygame-ce {pg.version.ver}, Python {python_version})")
    print(
        "Welcome to Fusion Engine! https://github.com/dimkauzh/fusion-engine. Check out our website at https://fusion-engine.tech/"
    )
