from sdl2 import *
import ctypes
import sdl2.ext
import threading
import time

class CustomRenderer:
    def __init__(self, window):
        self.window = window
        self.event = SDL_Event()
        self.renderer = SDL_CreateRenderer(self.window, -1, sdl2.SDL_RENDERER_ACCELERATED)

class Window:
    def __init__(self):
        self.window = None
        self.running = False
        
    def newWindow(self, title, width, height):
        encoded_title = title.encode('utf-8')
        self.window = SDL_CreateWindow(encoded_title, SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, width, height, SDL_WINDOW_SHOWN)
        self.running = True
        return CustomRenderer(self.window)
    
    def refresh(self, window):
        SDL_UpdateWindowSurface(window.window)
        SDL_RenderPresent(window.renderer)
        if sdl2.SDL_PollEvent(window.event) != 0:
            if window.event.type == sdl2.SDL_QUIT:
                self.running = False

        

    