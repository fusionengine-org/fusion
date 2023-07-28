from fusionengine.files.enums import RendererFlag
from fusionengine.files.imports import *


class RendererOptions:
    def __init__(self) -> None:
        self.rendererflag = sdl2.SDL_RENDERER_ACCELERATED

    def getSurfaceFromWindow(self, window):
        """Gets the surface from the window class. (Not for the user)"""
        return window.surface

    def setRendererFlag(self, flag: RendererFlag) -> None:
        """Sets the renderer flag. (Type of rendering)"""
        if flag == RendererFlag.PREVENT_SYNC:
            self.rendererflag = sdl2.SDL_RENDERER_PRESENTVSYNC
        elif flag == RendererFlag.SOFTWARE:
            self.rendererflag = sdl2.SDL_RENDERER_SOFTWARE
        elif flag == RendererFlag.TARGET_TEXTURE:
            self.rendererflag = sdl2.SDL_RENDERER_TARGETTEXTURE
        else:
            self.rendererflag = sdl2.SDL_RENDERER_ACCELERATED


class System:
    def __init__(self):
        pass
