from src.engine.files.enums import RendererFlag
from src.engine.files.imports import *

class RendererOptions:
    def __init__(self):
        self.rendererflag = SDL_RENDERER_ACCELERATED
    def getSurfaceFromWindow(self, window):
        return window.surface
    def setRendererFlag(self, flag):
        if flag == RendererFlag.PREVENT_SYNC:
            self.rendererflag = SDL_RENDERER_PRESENTVSYNC
        elif flag == RendererFlag.SOFTWARE:
            self.rendererflag = SDL_RENDERER_SOFTWARE
        elif flag == RendererFlag.TARGET_TEXTURE:
            self.rendererflag = SDL_RENDERER_TARGETTEXTURE
        else:
            self.rendererflag = SDL_RENDERER_ACCELERATED

class System:
    def __init__(self):
        pass
