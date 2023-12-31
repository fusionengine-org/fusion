import pygame as pg


class Sound:
    def __init__(self, sound_path: str) -> None:
        self.sound = pg.mixer.Sound(sound_path)

    def play(self):
        pg.mixer.Sound.play(self.sound)

    def stop(self):
        self.sound.stop()

    def get_volume(self):
        return self.sound.get_volume()

    def set_volume(self, volume: int):
        self.sound.set_volume(volume)

    def fadeout(self, time: int):
        self.sound.fadeout(time)

