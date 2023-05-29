from sdl2 import *
import ctypes
import sdl2.ext
from src.engine.files.window import *
from src.engine.files.draw import *
from src.engine.files.color import *

class Main:
    def __init__(self):
        SDL_Init(SDL_INIT_VIDEO)
        self.window = Window()
        self.draw = Draw()
        self.color = Colors()
        
    def Quit(self, window):
        SDL_FreeSurface(window.surface)
        SDL_DestroyWindow(window.window)
        SDL_Quit()
        
