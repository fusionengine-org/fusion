from src.engine.files.imports import *
import src.engine.files.systems as sysconfig

class Draw:
    def __init__(self):
        self.rendereroptions = sysconfig.RendererOptions()
    
    def drawLine(self, window, x1, y1, x2, y2, color):
        SDL_SetRenderDrawColor(window.renderer, color[0], color[1], color[2], color[3])
        SDL_RenderDrawLine(window.renderer, x1, y1, x2, y2) 
                
    def drawLineRect(self, renderer, x, y, width, height, color):
        rdr = window.renderer
        # Draw the top line
        self.drawLine(rdr, x, y, x + width, y, color)
        # Draw the bottom line
        self.drawLine(rdr, x, y + height, x + width, y + height, color)
        # Draw the left line
        self.drawLine(rdr, x, y, x, y + height, color)
        # Draw the right line
        self.drawLine(rdr, x + width, y, x + width, y + height, color)
        
    def drawRect(self, window, x, y, width, height, color):
        SDL_SetRenderDrawColor(window.renderer, color[0], color[1], color[2], color[3])
        rect = SDL_Rect(x, y, width, height)
        SDL_RenderFillRect(window.renderer, rect)

    def drawOwnRect(self, window, rect):
        SDL_SetRenderDrawColor(window.renderer, rect.color[0], rect.color[1], rect.color[2], rect.color[3])
        SDL_RenderFillRect(window.renderer, rect.rect)
    
    def setBackgroundColor(self, window, color):
        SDL_SetRenderDrawColor(window.renderer, color[0], color[1], color[2], color[3])
        SDL_RenderClear(window.renderer)
