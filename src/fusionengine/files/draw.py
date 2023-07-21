import fusionengine.files.systems as sysconfig
import fusionengine.files.window as window

from fusionengine.files.imports import *
import fusionengine.files.shape as shape


class Draw:
    def __init__(self) -> None:
        self.rendereroptions = sysconfig.RendererOptions()

    def draw_line(self, window: window._CustomRenderer, x1: int, y1: int, x2: int, y2: int, color: tuple) -> None:
        sdl2.SDL_SetRenderDrawColor(window.renderer,
                                    color[0],
                                    color[1],
                                    color[2],
                                    color[3]
                                    )

        sdl2.SDL_RenderDrawLine(window.renderer, x1, y1, x2, y2)

    def draw_line_rect(self, window: window._CustomRenderer, x: int, y: int, width: int, height: int, color: tuple) -> None:
        rdr = window.renderer
        self.draw_line(rdr, x, y, x + width, y, color)
        self.draw_line(rdr, x, y + height, x + width, y + height, color)
        self.draw_line(rdr, x, y, x, y + height, color)
        self.draw_line(rdr, x + width, y, x + width, y + height, color)

    def draw_rect(self, window: window._CustomRenderer, x: int, y: int, width: int, height: int, color: tuple) -> None:
        sdl2.SDL_SetRenderDrawColor(window.renderer,
                                    color[0],
                                    color[1],
                                    color[2],
                                    color[3]
                                    )

        rect = sdl2.SDL_Rect(x, y, width, height)
        sdl2.SDL_RenderFillRect(window.renderer, rect)

    def draw_own_rect(self, window: window._CustomRenderer, rect: shape._CustomShape) -> None:
        sdl2.SDL_SetRenderDrawColor(window.renderer,
                                    rect.color[0],
                                    rect.color[1],
                                    rect.color[2],
                                    rect.color[3]
                                    )

        sdl2.SDL_RenderFillRect(window.renderer, rect.rect)

    def set_background_color(self, window: window._CustomRenderer, color: tuple) -> None:
        sdl2.SDL_SetRenderDrawColor(window.renderer,
                                    color[0],
                                    color[1],
                                    color[2],
                                    color[3]
                                    )

        sdl2.SDL_RenderClear(window.renderer)
