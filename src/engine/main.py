from engine.files.imports import *
import engine.files.systems as sysconfig
import engine.files.data as data

class Main:
    def __init__(self):
        SDL_Init(SDL_INIT_VIDEO)
        self.window = window.Window()
        self.color = color.Colors()
        self.event = event.Event()
        self.keys = event.Keys()
        self.draw = draw.Draw()
        self.image = image.Image()
        self.body = body
        self.system = sysconfig.System()
        self.rendereroptions = sysconfig.RendererOptions()
        self.shape = shape.Shapes()
        
        self.DEBUGIMAGE = "engine/debugfiles/test.png"

    def quit(self, window):
        SDL_DestroyRenderer(window.renderer)
        SDL_DestroyWindow(window.window)
        del window
        SDL_Quit()
