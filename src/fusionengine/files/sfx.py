import fusionengine as fusion


class SfxLib:
    def __init__(self):
        """A class that contains all the free to use sound files."""
        self.SLAP = fusion.__path__[0] + "/sfx-lib/slap.mp3"
        self.SLIP = fusion.__path__[0] + "/sfx-lib/slip.mp3"
        self.SPLASH = fusion.__path__[0] + "/sfx-lib/splash.mp3"
