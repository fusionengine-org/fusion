import fusionengine.files.systems as sysconfig
from fusionengine.files.imports import *


class _CustomRenderer:
    def __init__(self, window: pg.Surface, title: str, width: int, height: int) -> None:
        """A class that creates a new custom renderer. (Not for the user)

        Args:
            window (sdl2.SDL_CreateWindow): An created sdl2 window
        """
        self.window = window

        self.title = title
        self.width = width
        self.height = height
        self.size = (self.width, self.height)


class Window:
    def __init__(self) -> None:
        """A class that contains all the window functions."""
        self._running = False
        self._fps = 60
        self.clock = pg.time.Clock()

    def new_window(self, title: str, width: int, height: int) -> _CustomRenderer:
        """Creates a new window.

        Args:
            title (str): Your window title
            width (int): Your window width
            height (int): Your window height

        Returns:
            window: Custom window class with all you need features
        """
        try:
            window_window = pg.display.set_mode((width, height))
            pg.display.set_caption(title)
            self._running = True
            self.window = _CustomRenderer(window_window, title, width, height)

        except Exception:
            print("Error: Can't create a window.")

        return self.window

    def loop(self, your_loop) -> None:
        """A while loop decorator function.

        Args:
            your_loop (callable): Your main loop function
        """
        while self.running(self.window):
            your_loop()

    def running(self, window: _CustomRenderer) -> bool:
        """Returns if the window is running. Used for the main loop.

        Args:
            window: Your window

        Returns:
            bool: returns true if the window is running else false
        """
        self._refresh(window)
        return self._running

    def set_fps(self, fps: int) -> None:
        """Sets the desired frames per second for the game loop.

        Args:
            fps (int): The desired frames per second
        """
        self._fps = fps

    def _refresh(self, window: _CustomRenderer) -> None:
        """Does all things for refreshing window. (Not for the user)

        Args:
            window: Your window
        """

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self._running = False

        pg.display.flip()

        self.DELTATIME = self.clock.tick(self._fps)
