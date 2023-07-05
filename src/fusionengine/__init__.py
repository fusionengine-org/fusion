__author__ = "Dimkauzh"
__version__ = "0.2.0"

import fusionengine.files.data as data
import fusionengine.files.systems as sysconfig

from fusionengine.files.imports import *

class Main:
    def __init__(self):
        SDL_Init(SDL_INIT_VIDEO)
        self.window = window.Window()
        self.color = color.Colors()
        self.event = event.Event()
        self.keys = event.Keys()
        self.draw = draw.Draw()
        self.image = image.Image()
        self.body = body
        self.system = sysconfig.System()
        self.rendereroptions = sysconfig.RendererOptions()
        self.shape = shape.Shapes()
        
        self.DEBUGIMAGE = "src/fusionengine/debugfiles/test.png"

    def quit(self, window):
        SDL_DestroyRenderer(window.renderer)
        SDL_DestroyWindow(window.window)
        del window
        SDL_Quit()
