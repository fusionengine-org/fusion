from sdl2 import *
import ctypes

class RendererOptions:
    
    def getSurfaceFromWindow(self, window):
        return window.surface