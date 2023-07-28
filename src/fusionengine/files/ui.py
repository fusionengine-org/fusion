from fusionengine.files.imports import *
import fusionengine.files.draw as draw
import fusionengine.files.window as windowfe


class _CustomButton:
    def __init__(
        self,
        window: window._CustomRenderer,
        text: str,
        x: int,
        y: int,
        width: int,
        height: int,
        font_path: str,
        font_sharp: int,
        centre: int,
        color_input: tuple,
    ) -> None:
        """A class that creates a new custom button. (Not for the user)"""
        self.window: windowfe._CustomRenderer = window
        self.text: str = text
        self.x: int = x
        self.y: int = y
        self.width = width
        self.height = height
        self.font_path = font_path
        self.font_size_input = font_sharp
        self.color = (color_input[0], color_input[1], color_input[2], color_input[3])
        self.is_pressed = False

        if self.font_size_input == "default":
            font_size = 1000
        else:
            font_size = font_sharp

        draw.Draw().draw_rect(window, x, y, width, height, self.color)

        sdl2.sdlttf.TTF_Init()
        self.font = sdl2.sdlttf.TTF_OpenFont(font_path.encode("utf-8"), font_size)

        text_surface = sdl2.sdlttf.TTF_RenderText_Solid(
            self.font, text.encode(), sdl2.SDL_Color(0, 0, 0)
        )
        self.texture = sdl2.SDL_CreateTextureFromSurface(
            self.window.renderer, text_surface
        )
        text_rect = sdl2.SDL_Rect(
            x + centre, y + centre, width - centre * 2, height - centre * 2
        )
        sdl2.SDL_RenderCopy(self.window.renderer, self.texture, None, text_rect)

        sdl2.sdlttf.TTF_CloseFont(self.font)
        sdl2.SDL_FreeSurface(text_surface)
        sdl2.sdlttf.TTF_Quit()

    def _handle_event(self) -> bool:
        """Handles the event of the mouse."""
        event = self.window.event
        _pressed = False
        if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.button.x, event.button.y
            if (
                self.x <= mouse_x <= self.x + self.width
                and self.y <= mouse_y <= self.y + self.height
            ):
                _pressed = True
        elif event.type == sdl2.SDL_MOUSEBUTTONUP:
            _pressed = False

        return _pressed

    def is_button_pressed(self) -> bool:
        """Returns if the button is pressed."""
        return self._handle_event()

    def set_color(self, color: tuple) -> None:
        """Sets the color of the buttons background."""
        self.color = color

    def button_pressed(self, func: callable) -> None:
        """Custom decorator function that executes a function when the button is pressed."""
        if self.is_button_pressed() and callable(func):
            func()


class Button:
    def __init__(self) -> None:
        pass

    def new_button(
        self,
        window: window._CustomRenderer,
        text: str,
        x: int,
        y: int,
        width: int,
        height: int,
        font_path: str,
        font_sharp: int,
        centre: int,
        color: tuple,
    ) -> _CustomButton:
        """Creates a new button for your ui."""
        return _CustomButton(
            window, text, x, y, width, height, font_path, font_sharp, centre, color
        )


class Text:
    def __init__(self) -> None:
        pass

    def print_text(
        self,
        window: window._CustomRenderer,
        text: str,
        x: int,
        y: int,
        width: int,
        height: int,
        font_path: str,
        font_sharp: int,
        color: tuple,
    ) -> None:
        """Prints text on the screen."""
        sdl2.sdlttf.TTF_Init()
        self.font = sdl2.sdlttf.TTF_OpenFont(font_path.encode("utf-8"), font_sharp)
        sdl2.SDL_SetRenderDrawColor(
            window.renderer, color[0], color[1], color[2], color[3]
        )

        text_surface = sdl2.sdlttf.TTF_RenderText_Solid(
            self.font,
            text.encode(),
            sdl2.SDL_Color(color[0], color[1], color[2], color[3]),
        )
        self.texture = sdl2.SDL_CreateTextureFromSurface(window.renderer, text_surface)
        text_rect = sdl2.SDL_Rect(x, y, width, height)
        sdl2.SDL_RenderCopy(window.renderer, self.texture, None, text_rect)

        sdl2.sdlttf.TTF_CloseFont(self.font)
        sdl2.SDL_FreeSurface(text_surface)
        sdl2.sdlttf.TTF_Quit()


class UI:
    def __init__(self) -> None:
        """A class that creates a new ui."""
        self.button = Button()
        self.text = Text()
