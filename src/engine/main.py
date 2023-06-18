from src.engine.files.imports import *
import src.engine.files.systems as sysconfig

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
        
        self.DEBUGIMAGE = "src/engine/debugfiles/test.png"

    def Quit(self, window):
        SDL_DestroyRenderer(window.renderer)
        SDL_FlushEvent(window.event)
        SDL_DestroyWindow(window.window)
        SDL_Quit()
