import pygame as pg


clicked = False


def key_down(key):
    keys = pg.key.get_pressed()
    return keys[key]


def key_down_once(key):
    global clicked
    if key_down(key) and not clicked:
        clicked = True
        return True
    elif not key_down(key):
        clicked = False
        return False



