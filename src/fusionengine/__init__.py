__author__ = "Dimkauzh"
__version__ = "1.1.2"

from fusionengine.files.imports import *
import fusionengine.files.systems as sysconfig


class Main:
    def __init__(self, *args) -> None:
        """A class that contains all the functions for the engine."""
        pg.init()

        self.window = window.Window()
        self.color = color.Colors()
        self.colortools = color.ColorTools()
        self.event = event.Event()
        self.keys = event.Keys()
        self.draw = draw.Draw()
        self.image = image.Image()
        self.body = body
        self.system = sysconfig.System()
        self.shape = shape.Shapes()
        self.ui = ui.UI()
        self.fonts = fonts.Fonts()
        self.debug = debug.DebugFiles()
        self.vector = vector.Vectors()

        if args != ("message=False",):
            python_version = sys.version.split()[0]
            print(
                f"Fusion Engine {__version__} (Pygame-ce {pg.version.ver}, Python {python_version})"
            )
            print("Welcome to Fusion Engine! https://github.com/dimkauzh/fusion-engine")
