def hex_to_rgba(hex):
    """Converts (#)RRGGBB to [R, G, B, 255].
    
    args:
        Hex: Your hex color
    """

    hex6 = hex.replace("#", "")
    return int(hex6[:2], 16), int(hex6[2:4], 16), int(hex6[4:6], 16), 255


def hsv_to_rgb(hue, sat, val, alpha: int) -> tuple[int, int, int, int]:
    """Takes in HSV values and ouputs red, green and blue values.
    Hue is from 0 to 360 (float).
    Saturation and value are from 0 to 1 (float).
    Alpha is from 0 to 255 (int).
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
