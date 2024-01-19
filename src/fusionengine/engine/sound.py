import pygame as pg


class Sound:
    def __init__(self, sound_path: str) -> None:
        """
        A class that creates a new sound.

        Args:
            sound_path (str): The path to the sound file
        """
        self.sound = pg.mixer.Sound(sound_path)

    def play(self) -> None:
        """
        Plays the sound
        """
        pg.mixer.Sound.play(self.sound)

    def stop(self) -> None:
        """
        Stops the sound
        """
        self.sound.stop()

    def get_volume(self) -> float:
        """
        Returns the volume of the sound

        Returns:
            float: The volume of the sound
        """
        return self.sound.get_volume()

    def set_volume(self, volume: int) -> None:
        """
        Send the volume of the sound

        Args:
            volume (int): The volume of the sound
        """
        self.sound.set_volume(volume)

    def fadeout(self, time: int) -> None:
        """
        Fadeout the sound

        Args:
            time (int): The time it takes to fadeout the sound
        """
        self.sound.fadeout(time)


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
