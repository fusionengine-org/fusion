from src.engine.files.imports import *
import src.engine.files.systems as sysconfig

class _CustomRenderer:
    def __init__(self, window):
        self.window = window
        self.event = SDL_Event()
        self.renderer = SDL_CreateRenderer(self.window, -1, sysconfig.RendererOptions().rendererflag)

class Window:
    def __init__(self):
        self.window = None
        self._running = False
        
        
    def newWindow(self, title, width, height):
        encoded_title = title.encode('utf-8')
        self.window = SDL_CreateWindow(encoded_title, SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, width, height, SDL_WINDOW_SHOWN)
        self._running = True
        return _CustomRenderer(self.window)
    
    def running(self, window):
        self._refresh(window)
        return self._running
    
    def _refresh(self, window):
        SDL_UpdateWindowSurface(window.window)
        SDL_RenderPresent(window.renderer)
        if sdl2.SDL_PollEvent(window.event) != 0:
            if window.event.type == sdl2.SDL_QUIT:
                self._running = False

        

    