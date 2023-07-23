import fusionengine.files.systems as sysconfig
from fusionengine.files.imports import *

class _CustomRenderer:
    def __init__(self, window: sdl2.SDL_CreateWindow) -> None:
        self.window = window
        self.event = sdl2.SDL_Event()
        self.renderer = sdl2.SDL_CreateRenderer(self.window, -1, sysconfig.RendererOptions().rendererflag)

class Window:
    def __init__(self) -> None:
        self._running = False
        self._NOW = sdl2.SDL_GetPerformanceCounter()
        self._LAST = 0
        self.DELTATIME = 0
        self._entity = []

    def new_window(self, title: str, width: int, height: int) -> _CustomRenderer:
        encoded_title = title.encode('utf-8')
        self.window_window = sdl2.SDL_CreateWindow(encoded_title,
                                       sdl2.SDL_WINDOWPOS_CENTERED,
                                       sdl2.SDL_WINDOWPOS_CENTERED,
                                       width,
                                       height,
                                       sdl2.SDL_WINDOW_SHOWN
                                       )
        self._running = True
        self.window = _CustomRenderer(self.window_window)

        return self.window

    def loop(self, your_loop):
        while self._running:
            self._refresh(self.window)
            your_loop()

    def running(self, window:_CustomRenderer) -> bool:
        self._refresh(window)
        return self._running

    def _refresh(self, window: _CustomRenderer) -> None:
        self.window = window

        sdl2.SDL_UpdateWindowSurface(window.window)
        sdl2.SDL_RenderPresent(window.renderer)

        sdl2.SDL_SetRenderDrawColor(self.window.renderer, 0, 0, 0, 255)
        sdl2.SDL_RenderClear(self.window.renderer)


        self._LAST = self._NOW
        self._NOW = sdl2.SDL_GetPerformanceCounter()

        self.DELTATIME = (self._NOW - self._LAST)*1000 / sdl2.SDL_GetPerformanceFrequency()

        if sdl2.SDL_PollEvent(window.event) != 0 and window.event.type == sdl2.SDL_QUIT:
            self._running = False
