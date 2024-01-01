import pygame as pg
from fusionengine.tools.deprecations import deprecated


clicked = False

class Key:
    def __init__(self, key) -> None:
        self.key = key

    def key_down(self):
        keys = pg.key.get_pressed()
        return keys[self.key]


    def key_down_once(self):
        if self.key_down() and not self.clicked:
            self.clicked = True
            return True
        elif not self.key_down():
            self.clicked = False
            return False

@deprecated(version="5.0.0")
def key_down(key):
    keys = pg.key.get_pressed()
    return keys[key]

@deprecated(version="5.0.0")
def key_down_once(key):
    global clicked
    if key_down(key) and not clicked:
        clicked = True
        return True
    elif not key_down(key):
        clicked = False
        return False


