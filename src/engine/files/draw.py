from engine.files.imports import *
import engine.files.systems as sysconfig

class Draw:
    def __init__(self):
        self.rendereroptions = sysconfig.RendererOptions()
    
    def drawLine(self, window, x1, y1, x2, y2, color):
        SDL_SetRenderDrawColor(window.renderer,
                               color[0],
                               color[1],
                               color[2],
                               color[3]
                               )

        SDL_RenderDrawLine(window.renderer, x1, y1, x2, y2) 
                
    def drawLineRect(self, window, x, y, width, height, color):
        rdr = window.renderer
        self.drawLine(rdr, x, y, x + width, y, color)
        self.drawLine(rdr, x, y + height, x + width, y + height, color)
        self.drawLine(rdr, x, y, x, y + height, color)
        self.drawLine(rdr, x + width, y, x + width, y + height, color)
        
    def drawRect(self, window, x, y, width, height, color):
        SDL_SetRenderDrawColor(window.renderer,
                               color[0],
                               color[1],
                               color[2],
                               color[3]
                               )

        rect = SDL_Rect(x, y, width, height)
        SDL_RenderFillRect(window.renderer, rect)

    def drawOwnRect(self, window, rect):
        SDL_SetRenderDrawColor(window.renderer,
                               rect.color[0],
                               rect.color[1],
                               rect.color[2],
                               rect.color[3]
                               )

        SDL_RenderFillRect(window.renderer, rect.rect)
    
    def setBackgroundColor(self, window, color):
        SDL_SetRenderDrawColor(window.renderer,
                               color[0],
                               color[1],
                               color[2],
                               color[3]
                               )

        SDL_RenderClear(window.renderer)
