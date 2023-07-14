from operator import is_
from fusionengine.files.imports import *
import fusionengine.files.draw as draw

class CustomButton:
    def __init__(self, window, text, x, y, width, height, font_path_input, font_size_input, color, function_button):
        self.window = window
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_path_input = font_path_input
        self.font_size_input = font_size_input
        self.color = color
        self.function_button = function_button
        self._background_color = (color[0], color[1], color[2], color[3])
        self.is_pressed = False
    
        if font_path_input == "default":
            font_path = "src/fusionengine/fonts/nunito_sans_light.ttf"
        else:
            font_path = font_path_input
        if font_size_input == "default":
            font_size = 1000
        else:
            font_size = font_size_input

        draw.Draw().draw_rect(window, x, y, width, height, self._background_color)

        sdl2.sdlttf.TTF_Init()
        self.font = sdl2.sdlttf.TTF_OpenFont(font_path.encode("utf-8"), font_size)

        text_surface = sdl2.sdlttf.TTF_RenderText_Solid(self.font, text.encode(), sdl2.SDL_Color(0, 0, 0))
        self.texture = sdl2.SDL_CreateTextureFromSurface(self.window.renderer, text_surface)
        text_rect = sdl2.SDL_Rect(x, y, width, height)
        sdl2.SDL_RenderCopy(self.window.renderer, self.texture, None, text_rect)

        sdl2.sdlttf.TTF_CloseFont(self.font)
        sdl2.SDL_FreeSurface(text_surface)
        sdl2.sdlttf.TTF_Quit()

        if self.is_button_pressed() and callable(function_button):
            function_button()

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

class Button:
    def __init__(self):
        self.color = None

    def new_button(self, window, text, x, y, width, height, font_path, font_size, color, function_button):
        return CustomButton(window, text, x, y, width, height, font_path, font_size, color, function_button)

class Text:
    def __init__(self):
        pass
class UI:
    def __init__(self):
        self.button = Button()
        self.text = Text()




        
        
