import tkinter as tk

class CustomItems:
    def __init__(self, window) -> None:
        self.window = window
    
    def new_label(self, text: str) -> tk.Label:
        label = tk.Label(self.window, text=text)
        label.pack()
        return label
    
    def new_button(self, text: str, function) -> tk.Button:
        button = tk.Button(self.window, text=text, function=function)
        button.pack()
        return button

class MenuItems:
    def __init__(self, window) -> None:
        self.window = window
    
    def get_center_window(self):
        # get the screen dimension
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        # find the center point
        center_x = int(self.screen_width/2 - self.screen_width / 2)
        center_y = int(self.screen_height/2 - self.screen_height / 2)
        
        return center_x, center_y

    def load_icon(self, file):
        icon = tk.PhotoImage(file = file)
        self.window.iconphoto(False, icon)

class Menu:
    def __init__(self):
        self.window = tk.Tk()
        self.labels = []
        
        self.ci = CustomItems(self.window)
        self.mi = MenuItems(self.window)
        
        self.window_width = 800
        self.window_height = 600
        self.window_center = self.mi.get_center_window()
        
        self.start()
        
    def start(self):
        self.window.geometry(f"{self.window_width}x{self.window_height}+{self.window_center[0]}+{self.window_center[1]}")
        self.window.title('Fusion-Engine')
        self.mi.load_icon("src/gui/assets/icon/fe.png")
        
        message = self.ci.new_label("Fusion-Engine")
        
        self.window.mainloop()
        

if __name__ == "__main__":
    menu = Menu()
