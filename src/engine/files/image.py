from engine.files.imports import *

class CustomImage:
    def __init__(self, window, texture, rect) -> None:
        self.window = window
        self.renderer = window.renderer
        self.texture = texture
        self.rect = rect

class Image: 
    def openImage(self, window, image, x:int, y:int, width:int, height:int) -> CustomImage:
        image = sdl2.ext.load_image(image)
        texture = sdl2.SDL_CreateTextureFromSurface(window.renderer, image)
        rect = sdl2.SDL_Rect(x, y, width, height)
        return CustomImage(window, texture, rect)
    
    def drawImage(self, image) -> None:
        sdl2.SDL_RenderClear(image.renderer)
        sdl2.SDL_RenderCopy(image.renderer, image.texture, None, image.rect)