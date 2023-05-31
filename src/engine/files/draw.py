from sdl2 import *
import ctypes
import sdl2.ext
import src.engine.files.system as config


class Draw:
    def __init__(self):
        self.rendereroptions = config.RendererOptions()
    
    def setPixel(self, window, x, y, color):
        surface = self.rendereroptions.getSurfaceFromWindow(window)
        sdl2.ext.fill(surface, color, (x, y, 1, 1))
        
    def drawLine(self, window, x1, y1, x2, y2, color):
        surface = self.rendereroptions.getSurfaceFromWindow(window)
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
        for i in range(x, x + width):
            for j in range(y, y + height):
                self.setPixel(window, i, j, color)