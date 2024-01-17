class Color:
    def __init__(self, r: int, g: int, b: int, a: int) -> None:
        """
        Creates a color object.

        Args:
            color (tuple[int, int, int, int]): The color in RGBA format
        """
        self.list = [r, g, b, a]
        self.r = r
        self.g = g
        self.b = b
        self.a = a


def hex_to_rgba(hex: str) -> tuple[int, int, int, int]:
    """
    Converts (#)RRGGBB to [R, G, B, 255].

    Args:
        Hex: Your hex color
    """

    hex6 = hex.replace("#", "")
    return int(hex6[:2], 16), int(hex6[2:4], 16), int(hex6[4:6], 16), 255


def hsv_to_rgb(
    hue: float, sat: float, val: float, alpha: int
) -> tuple[int, int, int, int]:
    """
    Takes in HSV values and ouputs red, green and blue values.

    Args:
        hue (float): Hue is from 0 to 360.
        sat (float): Saturation and value are from 0 to 1.
        val (float): Value is from 0 to 1.
        alpha (int): Alpha is from 0 to 255 (int).

    Returns:
        tuple[int, int, int, int]: RBGA format, that can be used in the engine
    """

    hue_red = 0
    hue_green = 0
    hue_blue = 0

    if hue <= 60:
        hue_red = 255

    elif 60 <= hue <= 120:
        hue_red = 255 * ((-hue / 60) + 2)

    elif 120 <= hue <= 240:
        hue_red = 0

    elif 240 <= hue <= 300:
        hue_red = (hue / 60) - 4

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
