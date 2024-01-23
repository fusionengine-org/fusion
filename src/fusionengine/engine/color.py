class Color:
    def __init__(self, r: int, g: int, b: int, a: int) -> None:
        """
        Creates a color object.

        Args:
            color (tuple[int, int, int, int]): The color in RGBA format
        """
        self.tuple = (r, g, b, a)
        self.r = r
        self.g = g
        self.b = b
        self.a = a


def hex_to_rgba(hex: str) -> Color:
    """
    Converts (#)RRGGBB to Fusion Color.

    Args:
        hex (str): Your hex color

    Returns:
        Color: The Fusion Color
    """

    hex6 = hex.replace("#", "")
    return Color(int(hex6[:2], 16), int(hex6[2:4], 16), int(hex6[4:6], 16), 255)


def hsv_to_rgb(hue: float, sat: float, val: float, alpha: int) -> Color:
    """
    Takes in HSV values and ouputs a Fusion Color

    Args:
        hue (float): Hue is from 0 to 360.
        sat (float): Saturation and value are from 0 to 1.
        val (float): Value is from 0 to 1.
        alpha (int): Alpha is from 0 to 255 (int).

    Returns:
        Color: RBGA format, that can be used in the engine
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

    return Color(int(red), int(green), int(blue), alpha)


ALICEBLUE = Color(240, 248, 255, 255)
ANTIQUEWHITE = Color(250, 235, 215, 255)
AQUA = Color(0, 255, 255, 255)
AQUAMARINE = Color(127, 255, 212, 255)
AZURE = Color(240, 255, 255, 255)
BEIGE = Color(245, 245, 220, 255)
BISQUE = Color(255, 228, 196, 255)
BLACK = Color(0, 0, 0, 255)
BLANCHEDALMOND = Color(255, 235, 205, 255)
BLUE = Color(0, 0, 255, 255)
BLUEVIOLET = Color(138, 43, 226, 255)
BROWN = Color(165, 42, 42, 255)
BURLYWOOD = Color(222, 184, 135, 255)
CADETBLUE = Color(95, 158, 160, 255)
CHARTREUSE = Color(127, 255, 0, 255)
CHOCOLATE = Color(210, 105, 30, 255)
CORAL = Color(255, 127, 80, 255)
CORNFLOWERBLUE = Color(100, 149, 237, 255)
CORNSILK = Color(255, 248, 220, 255)
CRIMSON = Color(220, 20, 60, 255)
CYAN = Color(0, 255, 255, 255)
DARKBLUE = Color(0, 0, 139, 255)
DARKCYAN = Color(0, 139, 139, 255)
DARKGOLDENROD = Color(184, 134, 11, 255)
DARKGRAY = Color(169, 169, 169, 255)
DARKGREEN = Color(0, 100, 0, 255)
DARKKHAKI = Color(189, 183, 107, 255)
DARKMAGENTA = Color(139, 0, 139, 255)
DARKOLIVEGREEN = Color(85, 107, 47, 255)
DARKORANGE = Color(255, 140, 0, 255)
DARKORCHID = Color(153, 50, 204, 255)
DARKRED = Color(139, 0, 0, 255)
DARKSALMON = Color(233, 150, 122, 255)
DARKSEAGREEN = Color(143, 188, 143, 255)
DARKSLATEBLUE = Color(72, 61, 139, 255)
DARKSLATEGRAY = Color(47, 79, 79, 255)
DARKTURQUOISE = Color(0, 206, 209, 255)
DARKVIOLET = Color(148, 0, 211, 255)
DEEPPINK = Color(255, 20, 147, 255)
DEEPSKYBLUE = Color(0, 191, 255, 255)
DIMGRAY = Color(105, 105, 105, 255)
DODGERBLUE = Color(30, 144, 255, 255)
FIREBRICK = Color(178, 34, 34, 255)
FLORALWHITE = Color(255, 250, 240, 255)
FORESTGREEN = Color(34, 139, 34, 255)
FUCHSIA = Color(255, 0, 255, 255)
GAINSBORO = Color(220, 220, 220, 255)
GHOSTWHITE = Color(248, 248, 255, 255)
GOLD = Color(255, 215, 0, 255)
GOLDENROD = Color(218, 165, 32, 255)
GRAY = Color(128, 128, 128, 255)
GREEN = Color(0, 128, 0, 255)
GREENYELLOW = Color(173, 255, 47, 255)
HONEYDEW = Color(240, 255, 240, 255)
HOTPINK = Color(255, 105, 180, 255)
INDIANRED = Color(205, 92, 92, 255)
INDIGO = Color(75, 0, 130, 255)
IVORY = Color(255, 255, 240, 255)
KHAKI = Color(240, 230, 140, 255)
LAVENDER = Color(230, 230, 250, 255)
LAVENDERBLUSH = Color(255, 240, 245, 255)
LAWNGREEN = Color(124, 252, 0, 255)
LEMONCHIFFON = Color(255, 250, 205, 255)
LIGHTBLUE = Color(173, 216, 230, 255)
LIGHTCORAL = Color(240, 128, 128, 255)
LIGHTCYAN = Color(224, 255, 255, 255)
LIGHTGOLDENRODYELLOW = Color(250, 250, 210, 255)
LIGHTGRAY = Color(211, 211, 211, 255)
LIGHTGREEN = Color(144, 238, 144, 255)
LIGHTSALMON = Color(255, 182, 193, 255)
LIGHTSEAGREEN = Color(32, 178, 170, 255)
LIGHTSKYBLUE = Color(135, 206, 250, 255)
LIGHTSLATEGRAY = Color(119, 136, 153, 255)
LIGHTSTEELBLUE = Color(176, 196, 222, 255)
LIGHTYELLOW = Color(255, 255, 224, 255)
LIME = Color(0, 255, 0, 255)
LIMEGREEN = Color(50, 205, 50, 255)
LINEN = Color(250, 240, 230, 255)
MAGENTA = Color(255, 0, 255, 255)
MAROON = Color(128, 0, 0, 255)
MEDIUMAQUAMARINE = Color(102, 205, 170, 255)
MEDIUMBLUE = Color(0, 0, 205, 255)
MEDIUMORCHID = Color(186, 85, 211, 255)
MEDIUMPURPLE = Color(147, 112, 219, 255)
MEDIUMSEAGREEN = Color(60, 179, 113, 255)
MEDIUMSLATEBLUE = Color(123, 104, 238, 255)
MEDIUMSPRINGGREEN = Color(0, 250, 154, 255)
MEDIUMTURQUOISE = Color(72, 209, 204, 255)
MEDIUMVIOLETRED = Color(199, 21, 133, 255)
MIDNIGHTBLUE = Color(25, 25, 112, 255)
MINTCREAM = Color(245, 255, 250, 255)
MISTYROSE = Color(255, 228, 225, 255)
MOCCASIN = Color(255, 228, 181, 255)
NAVAJOWHITE = Color(255, 222, 173, 255)
NAVY = Color(0, 0, 128, 255)
OLDLACE = Color(253, 245, 230, 255)
OLIVE = Color(128, 128, 0, 255)
OLIVEDRAB = Color(107, 142, 35, 255)
ORANGE = Color(255, 165, 0, 255)
ORANGERED = Color(255, 69, 0, 255)
ORCHID = Color(218, 112, 214, 255)
PALEGOLDENROD = Color(238, 232, 170, 255)
PALEGREEN = Color(152, 251, 152, 255)
PALETURQUOISE = Color(175, 238, 238, 255)
PALEVIOLETRED = Color(219, 112, 147, 255)
PAPAYAWHIP = Color(255, 239, 213, 255)
PEACHPUFF = Color(255, 218, 185, 255)
PERU = Color(205, 133, 63, 255)
PINK = Color(255, 192, 203, 255)
PLUM = Color(221, 160, 221, 255)
POWDERBLUE = Color(176, 224, 230, 255)
PURPLE = Color(128, 0, 128, 255)
REBECCAPURPLE = Color(102, 51, 153, 255)
RED = Color(255, 0, 0, 255)
ROSYBROWN = Color(188, 143, 143, 255)
ROYALBLUE = Color(65, 105, 225, 255)
SADDLEBROWN = Color(139, 69, 19, 255)
SALMON = Color(250, 128, 114, 255)
SANDYBROWN = Color(244, 164, 96, 255)
SEAGREEN = Color(46, 139, 87, 255)
SEASHELL = Color(255, 245, 238, 255)
SIENNA = Color(160, 82, 45, 255)
SILVER = Color(192, 192, 192, 255)
SKYBLUE = Color(135, 206, 235, 255)
SLATEBLUE = Color(106, 90, 205, 255)
SLATEGRAY = Color(112, 128, 144, 255)
SNOW = Color(255, 250, 250, 255)
SPRINGGREEN = Color(0, 255, 127, 255)
STEELBLUE = Color(70, 130, 180, 255)
TAN = Color(210, 180, 140, 255)
TEAL = Color(0, 128, 128, 255)
THISTLE = Color(216, 191, 216, 255)
TOMATO = Color(255, 99, 71, 255)
TURQUOISE = Color(64, 224, 208, 255)
VIOLET = Color(238, 130, 238, 255)
WHEAT = Color(245, 222, 179, 255)
WHITE = Color(255, 255, 255, 255)
WHITESMOKE = Color(245, 245, 245, 255)
YELLOW = Color(255, 255, 0, 255)
YELLOWGREEN = Color(154, 205, 50, 255)
