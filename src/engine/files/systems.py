from engine.files.imports import *
from engine.files.enums import RendererFlag

class RendererOptions:
    def __init__(self) -> None:
        self.rendererflag = SDL_RENDERER_ACCELERATED
    def getSurfaceFromWindow(self, window):
        return window.surface
    def setRendererFlag(self, flag: RendererFlag) -> None:
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
