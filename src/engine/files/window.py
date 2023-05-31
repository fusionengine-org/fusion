from sdl2 import *
import ctypes
import sdl2.ext

class CustomRenderer:
    def __init__(self, window):
        self.window = window
        self.surface = SDL_GetWindowSurface(window)

class Window:
    def __init__(self):
        self.window = None
        self.running = True
    
    def newWindow(self, title, width, height):
        self.window = SDL_CreateWindow(title.encode('utf-8'), SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, width, height, SDL_WINDOW_SHOWN)
        return CustomRenderer(self.window)

    
    def refresh(self, window):
        window = window.window
        SDL_UpdateWindowSurface(window)
        
        event = SDL_Event()
        if SDL_PollEvent(event) != 0:
            if event.type == SDL_QUIT:
                self.running = False