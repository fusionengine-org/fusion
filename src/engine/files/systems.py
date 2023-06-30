from engine.files.imports import *

class RendererOptions:
    def __init__(self):
        self.rendererflag = SDL_RENDERER_ACCELERATED
    def getSurfaceFromWindow(self, window):
        return window.surface
    def setRendererFlag(self, type):
        if type == "PRESENTVSYNC" or type == "presentvsync":
            self.rendererflag = SDL_RENDERER_PRESENTVSYNC
        elif type == "software" or type == "SOFTWARE":
            self.rendererflag = SDL_RENDERER_SOFTWARE
        elif type == "TARGETTEXTURE" or type == "targettexture":
            self.rendererflag = SDL_RENDERER_TARGETTEXTURE
        else:
            self.rendererflag = SDL_RENDERER_ACCELERATED

class System:
    def __init__(self):
        pass
