"""
A custom open-source game engine on Python and Pygame, it's written in pure Python! It's easy and fast!
"""
import tkinter as tk
import fusionengine_gui.menu as menu


def main():
    # This should start and launch your app!
    window = tk.Tk()
    window.title("Fusion Engine")
    window.geometry("1280x720")

    menu.Menu(window)

    window.mainloop()
