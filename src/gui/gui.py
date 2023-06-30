import tkinter as tk

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
        
    def get_center_window(self, window):
        # get the screen dimension
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - self.window_width / 2)
        center_y = int(screen_height/2 - self.window_height / 2)
        
        return center_x, center_y

    def load_icon(self):
        icon = tk.PhotoImage(file ="src/gui/assets/icon/fe.png")
        self.window.iconphoto(False, icon)

if __name__ == "__main__":
    menu = Menu()
