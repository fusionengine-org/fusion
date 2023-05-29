from sdl2 import *
import ctypes
import sdl2.ext

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