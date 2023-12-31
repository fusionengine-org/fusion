import pygame as pg

class BackgroundMusic:
    def __init__(self, sound_path):
        pg.mixer.music.load(sound_path)
        pg.mixer.music.play(-1)

    def set_volume(self, volume):
        pg.mixer.music.set_volume(volume)
