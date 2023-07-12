from fusionengine.files.imports import *
import fusionengine.files.draw as draw

class CustomButton:
    def __init__(self, window, text, x, y, width, height, font_path, font_size, color, function_button):
        self.window = window
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_path = font_path
        self.font_size = font_size
        self.color = color
        self.function_button = function_button
        self.background_color

class Button:
    def new_button(self, window,  text, x, y, width, height, font_path, font_size, color,  function_button):
        self.renderer = window.renderer
        self.window = window.window
        if font_path == "default":
            font_path = "src/fusionengine/fonts/nunito_sans_light.ttf"
        elif font_size == "default":
            font_size = 12

        draw.draw_rect(window, x, y, width, height, (255, 255, 255, 255))

        sdl2.sdlttf.TTF_Init()
        self.font = sdl2.sdlttf.TTF_OpenFont(font_path.encode(), font_size)

        text_surface = sdl2.sdlttf.TTF_RenderText_Solid(self.font, self.text.encode(), sdl2.SDL_Color(0, 0, 0))
        texture = sdl2.SDL_CreateTextureFromSurface(self.renderer, text_surface)
        text_rect = sdl2.SDL_Rect(x, y, width, height)
        sdl2.SDL_RenderCopy(self.renderer, texture, None, text_rect)

        sdl2.sdlttf.TTF_CloseFont(self.font)
        sdl2.SDL_FreeSurface(text_surface)
        sdl2.SDL_DestroyTexture(texture)

class Text:
    def __init__(self):
        pass
class UI:
    def __init__(self):
        self.button = Button()
        self.text = Text()




        
        
