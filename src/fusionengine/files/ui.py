from fusionengine.files.imports import *
import fusionengine.files.draw as draw

class CustomButton:
    def __init__(self, window, text, x, y, width, height, font_path, font_size_input, centre, color_input):
        self.window = window
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_path = font_path
        self.font_size_input = font_size_input
        self.color = (color_input[0], color_input[1], color_input[2], color_input[3])
        self.is_pressed = False
    
        if font_size_input == "default":
            font_size = 1000
        else:
            font_size = font_size_input

        draw.Draw().draw_rect(window, x, y, width, height, self.color)

        sdl2.sdlttf.TTF_Init()
        self.font = sdl2.sdlttf.TTF_OpenFont(font_path.encode("utf-8"), font_size)

        text_surface = sdl2.sdlttf.TTF_RenderText_Solid(self.font, text.encode(), sdl2.SDL_Color(0, 0, 0))
        self.texture = sdl2.SDL_CreateTextureFromSurface(self.window.renderer, text_surface)
        text_rect = sdl2.SDL_Rect(x + centre, y + centre, width - centre * 2, height - centre * 2)
        sdl2.SDL_RenderCopy(self.window.renderer, self.texture, None, text_rect)

        sdl2.sdlttf.TTF_CloseFont(self.font)
        sdl2.SDL_FreeSurface(text_surface)
        sdl2.sdlttf.TTF_Quit()

    def _handle_event(self):
        event = self.window.event
        _pressed = False
        if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.button.x, event.button.y
            if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
                _pressed = True
        elif event.type == sdl2.SDL_MOUSEBUTTONUP:
            _pressed = False

        return _pressed

    def is_button_pressed(self):
        return self._handle_event()
    
    def set_color(self, color):
        self.color = color

    def button_pressed(self, func):
        if self.is_button_pressed() and callable(func):
            func()

class Button:
    def __init__(self):
        pass

    def new_button(self, window, text, x, y, width, height, font_path, font_size, centre, color):
        return CustomButton(window, text, x, y, width, height, font_path, font_size, centre, color)

class Text:
    def __init__(self):
        pass

    def print_text(self, window, text, x, y, width, height, font_path, font_size, color):
        sdl2.sdlttf.TTF_Init()
        self.font = sdl2.sdlttf.TTF_OpenFont(font_path.encode("utf-8"), font_size)
        sdl2.SDL_SetRenderDrawColor(window.renderer, color[0], color[1], color[2], color[3])

        text_surface = sdl2.sdlttf.TTF_RenderText_Solid(self.font, text.encode(), sdl2.SDL_Color(0, 0, 0))
        self.texture = sdl2.SDL_CreateTextureFromSurface(self.window.renderer, text_surface)
        text_rect = sdl2.SDL_Rect(x, y, width, height)
        sdl2.SDL_RenderCopy(self.window.renderer, self.texture, None, text_rect)

        sdl2.sdlttf.TTF_CloseFont(self.font)
        sdl2.SDL_FreeSurface(text_surface)
        sdl2.sdlttf.TTF_Quit()

class UI:
    def __init__(self):
        self.button = Button()
        self.text = Text()
