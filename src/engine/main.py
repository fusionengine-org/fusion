from sdl2 import *
import ctypes
import sdl2.ext


class CustomRenderer:
    def __init__(self, window):
        self.window = window
        self.surface = SDL_GetWindowSurface(window)

class Window:
    def __init__(self):
        self.window = None
        self.running = True
    
    def newWindow(self, title, width, height):
        self.window = SDL_CreateWindow(title.encode('utf-8'), SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, width, height, SDL_WINDOW_SHOWN)
        customrenderer = CustomRenderer(self.window)
        return customrenderer

    
    def refresh(self, window):
        SDL_UpdateWindowSurface(window)
        
        event = SDL_Event()
        if SDL_PollEvent(event) != 0:
            if event.type == SDL_QUIT:
                self.running = False

class Draw:

    def setPixel(self, surface, x, y, color, ):
        sdl2.ext.fill(surface, color, (x, y, 1, 1))
        
    def drawLine(self, surface, x1, y1, x2, y2, color):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        step_x = 1 if x1 < x2 else -1
        step_y = 1 if y1 < y2 else -1
        error = dx - dy

        while True:
            self.setPixel(surface, x1, y1, color)

            if x1 == x2 and y1 == y2:
                break

            error2 = 2 * error
            if error2 > -dy:
                error -= dy
                x1 += step_x
            if error2 < dx:
                error += dx
                y1 += step_y

class Main:
    def __init__(self):
        SDL_Init(SDL_INIT_VIDEO)
        self.window = Window()
        self.draw = Draw()
        self.BLUE = (0, 0, 255, 255)
        self.BLACK = (0, 0, 0, 255)
        self.WHITE = (255, 255, 255, 255)
        self.GREEN = (255, 255, 255, 255)
        self.RED = (255, 0, 0, 255)
        
    def Quit(self, window):
        SDL_FreeSurface(window.surface)
        SDL_DestroyWindow(window.window)
        SDL_Quit()
        
