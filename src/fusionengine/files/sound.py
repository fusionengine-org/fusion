from fusionengine.files.imports import *


class _CustomMusic:
    def __init__(self, sound_path) -> None:
        self.sound = pg.mixer.Sound(sound_path)

    def play(self):
        pg.mixer.Sound.play(self.sound)

    def stop(self):
        self.sound.stop()

    def get_volume(self):
        return self.sound.get_volume()

    def set_volume(self, volume):
        self.sound.set_volume(volume)

    def fadeout(self, time):
        self.sound.fadeout(time)


class Sound:
    def __init__(self) -> None:
        pass

    def load_sound(self, sound_path: str):
        return _CustomMusic(sound_path)

    def play_background_music(self, sound_path):
        pg.mixer.music.load(sound_path)
        pg.mixer.music.play(-1)

    def set_volume_global(self, volume):
        pg.mixer.music.set_volume(volume)
