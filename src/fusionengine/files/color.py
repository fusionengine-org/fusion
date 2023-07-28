class Colors:
    def __init__(self):
        """A class that contains all the colors in RGBA format."""
        self.BLUE = (0, 0, 255, 255)
        self.BLACK = (0, 0, 0, 255)
        self.WHITE = (255, 255, 255, 255)
        self.GREEN = (0, 255, 0, 255)
        self.RED = (255, 0, 0, 255)
        self.YELLOW = (255, 255, 0, 255)
        self.PURPLE = (128, 0, 128, 255)
        self.CYAN = (0, 255, 255, 255)
        self.ORANGE = (255, 165, 0, 255)
        self.GRAY = (128, 128, 128, 255)
        self.BROWN = (165, 42, 42, 255)
        self.PINK = (255, 192, 203, 255)
        self.MAGENTA = (255, 0, 255, 255)
        self.SILVER = (192, 192, 192, 255)
        self.GOLD = (255, 215, 0, 255)
        self.BRONZE = (205, 127, 50, 255)
        self.LIME = (0, 255, 0, 255)
        self.OLIVE = (128, 128, 0, 255)
        self.TEAL = (0, 128, 128, 255)
        self.NAVY = (0, 0, 128, 255)
        self.MAROON = (128, 0, 0, 255)
        self.INDIGO = (75, 0, 130, 255)
        self.TURQUOISE = (64, 224, 208, 255)
        self.VIOLET = (238, 130, 238, 255)
        self.AQUA = (0, 255, 255, 255)
        self.TAN = (210, 180, 140, 255)
        self.BEIGE = (245, 245, 220, 255)
        self.IVORY = (255, 255, 240, 255)
        self.LAVENDER = (230, 230, 250, 255)
        self.MINT = (189, 252, 201, 255)
        self.SALMON = (250, 128, 114, 255)
        self.SCARLET = (255, 36, 0, 255)
        self.TOMATO = (255, 99, 71, 255)


class ColorTools:
    def __init__(self):
        pass

    def hex_to_rgba(self, hex):
        """Converts (#)RRGGBB to [R, G, B, 255]."""
        hex6 = hex.replace("#", "")
        return int(hex6[:2], 16), int(hex6[2:4], 16), int(hex6[4:6], 16), 255
