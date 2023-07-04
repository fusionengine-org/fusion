import tkinter as tk

        
class MenuItems:
    def __init__(self, window) -> None:
        self.window = window
    
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
    
    def new_label(self, window, text) -> tk.Label:
        label = tk.Label(window, text=text)
        return label