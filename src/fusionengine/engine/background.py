import pygame as pg


class BackgroundMusic:
    def __init__(self, sound_path: str) -> None:
        """
        The class for background music.

        Args:
            sound_path (str): The path to the sound file
        """
        pg.mixer.music.load(sound_path)
        pg.mixer.music.play(-1)

    def set_volume(self, volume: int) -> None:
        """
        Sets the volume of the background music.

        Args:
            volume (int): The volume of the background music
        """
        pg.mixer.music.set_volume(volume)
