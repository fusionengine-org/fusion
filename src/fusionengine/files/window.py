import fusionengine.files.systems as sysconfig
from fusionengine.files.imports import *

class _CustomRenderer:
    def __init__(self, window: sdl2.SDL_CreateWindow) -> None:
        """A class that creates a new custom renderer. (Not for the user)

        Args:
            window (sdl2.SDL_CreateWindow): An created sdl2 window
        """        """"""
        self.window = window

        self.width = None
        self.height = None

        self.event = sdl2.SDL_Event()
        self.renderer = sdl2.SDL_CreateRenderer(self.window, -1, sysconfig.RendererOptions().rendererflag)
        sdl2.SDL_SetRenderDrawBlendMode(self.renderer, sdl2.SDL_BLENDMODE_BLEND)

        sdl2.SDL_GetWindowSize(self.window, self.width, self.height)
        self.title = sdl2.SDL_GetWindowTitle(self.window)

        self.size = (self.width, self.height)

class Window:
    def __init__(self) -> None:
        """A class that contains all the window functions.
        """        """"""
        self._running = False
        self._NOW = sdl2.SDL_GetPerformanceCounter()
        self._LAST = 0
        self.DELTATIME = 0
        self._entity = []

    def new_window(self, title: str, width: int, height: int) -> _CustomRenderer:
        """ Creates a new window.

        Args:
            title (str): Your window title
            width (int): Your window width
            height (int): Your window height

        Returns:
            window: Custom window class with all you need features
        """
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

    def loop(self, your_loop: callable):
        """A custom decorator function that turns a function into the main loop of the program.

        Args:
            your_loop (callable): Your main loop function (with decorator before it)
        """
        while self._running:
            self._refresh(self.window)
            your_loop()

    def running(self, window:_CustomRenderer) -> bool:
        """Returns if the window is running. Used for the main loop.

        Args:
            window: Your window

        Returns:
            bool: returns true if the window is running else false
        """        
        self._refresh(window)
        return self._running

    def _refresh(self, window: _CustomRenderer) -> None:
        """Does all things for refreshing window. (Not for the user)

        Args:
            window: Your window
        """        
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
