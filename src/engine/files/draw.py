from sdl2 import *
import ctypes
import sdl2.ext
import src.engine.files.system as config


class Draw:
    def __init__(self):
        self.rendereroptions = config.RendererOptions()
    
    def drawLine(self, window, x1, y1, x2, y2, color):
        pass
                
    def drawLineRect(self, window, x, y, width, height, color):
        surface = self.rendereroptions.getSurfaceFromWindow(window)
        # Draw the top line
        self.drawLine(surface, x, y, x + width, y, color)
        # Draw the bottom line
        self.drawLine(surface, x, y + height, x + width, y + height, color)
        # Draw the left line
        self.drawLine(surface, x, y, x, y + height, color)
        # Draw the right line
        self.drawLine(surface, x + width, y, x + width, y + height, color)
        
    def drawRect(self, window, x, y, width, height, color):
        SDL_RenderClear(window.renderer)
        SDL_SetRenderDrawColor(window.renderer, 255, 0, 0, 0)
        rect = SDL_Rect(x, y, width, height)
        SDL_RenderFillRect(window.renderer, rect)