from src.engine.files.imports import *

class Main:
    def __init__(self):
        SDL_Init(SDL_INIT_VIDEO)
        self.window = window.Window()
        self.color = color.Colors()
        self.event = event.Event()
        self.keys = event.Keys()
        self.draw = draw.Draw()
        self.image = image.Image()
        
        self.DEBUGIMAGE = "src/engine/debugfiles/test.png"
        self.get_delta_time.last_time = time.time()
        self.DELTATIME = self.getDeltaTime()

    def Quit(self, window):
        SDL_DestroyRenderer(window.renderer)
        SDL_FlushEvent(window.event)
        SDL_DestroyWindow(window.window)
        SDL_Quit()
    
    def getDeltaTime(self):
        current_time = time.time()
        delta_time = current_time - self.get_delta_time.last_time
        self.get_delta_time.last_time = current_time
        return delta_time
