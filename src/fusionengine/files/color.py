class Colors:
    def __init__(self):
        """A class that contains all the colors in RGBA format."""
        self.BLUE = 0, 0, 255, 255
        self.BLACK = 0, 0, 0, 255
        self.WHITE = 255, 255, 255, 255
        self.GREEN = 0, 255, 0, 255
        self.RED = 255, 0, 0, 255
        self.YELLOW = 255, 255, 0, 255
        self.PURPLE = 128, 0, 128, 255
        self.CYAN = 0, 255, 255, 255
        self.ORANGE = 255, 165, 0, 255
        self.GRAY = 128, 128, 128, 255
        self.BROWN = 165, 42, 42, 255
        self.PINK = 255, 192, 203, 255
        self.MAGENTA = 255, 0, 255, 255
        self.SILVER = 192, 192, 192, 255
        self.GOLD = 255, 215, 0, 255
        self.BRONZE = 205, 127, 50, 255
        self.CHARTREUSE = 128, 255, 0, 255
        self.OLIVE = 128, 128, 0, 255
        self.TEAL = 0, 128, 128, 255
        self.NAVY = 0, 0, 128, 255
        self.MAROON = 128, 0, 0, 255
        self.INDIGO = 75, 0, 130, 255
        self.TURQUOISE = 64, 224, 208, 255
        self.VIOLET = 238, 130, 238, 255
        self.AQUA = 0, 255, 255, 255
        self.TAN = 210, 180, 140, 255
        self.BEIGE = 245, 245, 220, 255
        self.IVORY = 255, 255, 240, 255
        self.LAVENDER = 230, 230, 250, 255
        self.MINT = 189, 252, 201, 255
        self.SALMON = 250, 128, 114, 255
        self.SCARLET = 255, 36, 0, 255
        self.TOMATO = 255, 99, 71, 255
        self.CRIMSON = 220, 20, 60, 255
        self.AZURE = 0, 128, 255, 255


class ColorTools:
    def __init__(self):
        pass
    
    @staticmethod
    def hex_to_rgba(self, hex):
        """Converts (#)RRGGBB to [R, G, B, 255]."""
        hex6 = hex.replace("#", "")
        return int(hex6[:2], 16), int(hex6[2:4], 16), int(hex6[4:6], 16), 255
    
    @staticmethod
    def hsv_to_rgb(hue, sat, val, alpha: int) -> tuple[int, int, int, int]:
        """Takes in HSV values and ouputs red, green and blue values.
        Hue is from 0 to 360 (float).
        Saturation and value are from 0 to 1 (float).
        Alpha is from 0 to 255 (int)."""
        if hue <= 60:
            hue_red = 255

        elif 60 <= hue <= 120:
            hue_red = 255 * ((-hue / 60) + 2)

        elif 120 <= hue <= 240:
            hue_red = 0

        elif 240 <= hue <= 300:
            hue_red = ((hue / 60) - 4)

        elif 300 <= hue <= 360:
            hue_red = 255

        if hue <= 60:
            hue_green = 255 * (hue / 60)

        elif 60 <= hue <= 180:
            hue_green = 255

        elif 180 <= hue <= 240:
            hue_green = 255 * ((-hue / 60) + 4)

        elif 240 <= hue <= 360:
            hue_green = 0

        if hue <= 120:
            hue_blue = 0

        elif 120 <= hue <= 180:
            hue_blue = 255 * ((hue / 60) - 2)

        elif 180 <= hue <= 300:
            hue_blue = 255

        elif 300 <= hue <= 360:
            hue_blue = 255 * ((-hue / 60) + 6)

        red = val * (sat * hue_red + (255 - 255 * sat))
        green = val * (sat * hue_green + (255 - 255 * sat))
        blue = val * (sat * hue_blue + (255 - 255 * sat))

        return int(red), int(green), int(blue), alpha
