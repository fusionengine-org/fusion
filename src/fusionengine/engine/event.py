import pygame as pg


class Key:
    key_states = {}

    def __init__(self, key) -> None:
        """
        The key class that handles key presses and key states.

        Args:
            key: The key you want to handle
        """
        self.key = key
        self.clicked = False

        if key not in Key.key_states:
            Key.key_states[key] = False

    def key_down(self) -> bool:
        """
        Checks if the key is pressed down.

        Returns:
            bool: True if the key is pressed down, False if not.
        """
        keys = pg.key.get_pressed()
        return keys[self.key]

    def key_down_once(self) -> bool:
        """
        Checks if the key is pressed down once.

        Returns:
            bool: Returns True once if the key is pressed down, Returns False if not.
        """
        if self.key_down() and not Key.key_states[self.key]:
            Key.key_states[self.key] = True
            return True
        elif not self.key_down() and Key.key_states[self.key]:
            Key.key_states[self.key] = False
        return False


def key_down(key) -> bool:
    """
    Checks if the key is pressed down.

    Returns:
        bool: True if the key is pressed down, False if not.
    """
    return Key(key).key_down()


def key_down_once(key) -> bool:
    """
    Checks if the key is pressed down once.

    Returns:
        bool: Returns True once if the key is pressed down, Returns False if not.
    """
    return Key(key).key_down_once()


def get_mouse_pos(self) -> tuple[int, int]:
    """
    Gets the mouse position.

    Returns:
        tuple: The mouse position
    """
    return pg.mouse.get_pos()
