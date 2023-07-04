import tkinter as tk
import src.gui.ui.main as ui


class Menu:
    def __init__(self):
        self.window = tk.Tk()
        self.labels = []
        
        self.window_width = 800
        self.window_height = 600
        self.window_center = self.get_center_window(self.window)
        
        self.start()
        
    def start(self):
        self.window.geometry(f"{self.window_width}x{self.window_height}+{self.window_center[0]}+{self.window_center[1]}")
        self.window.title('Fusion-Engine')
        self.load_icon()
        
        message = tk.Label(self.window, text="Hello, World!")
        self.labels.append(message)
        
        self.loop()
        
    def loop(self):
        for l in self.labels:
            l.pack()
        self.window.mainloop()
        

if __name__ == "__main__":
    menu = Menu()
