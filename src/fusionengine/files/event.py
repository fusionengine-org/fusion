from fusionengine.files.imports import *
import fusionengine.files.window as window


class Event:
    def __init__(self) -> None:
        pass

    def key_down_once(self, key: int, window: window._CustomRenderer) -> bool:
        return False

    def key_down(self, key, window):
        keys = pg.key.get_pressed()
        return keys[key]


class Keys:
    def __init__(self):
        """A class that contains all the keys."""
        self.KEY_UNKNOWN = pg.K_UNKNOWN
        self.KEY_RETURN = pg.K_RETURN
        self.KEY_ESCAPE = pg.K_ESCAPE
        self.KEY_BACKSPACE = pg.K_BACKSPACE
        self.KEY_TAB = pg.K_TAB
        self.KEY_SPACE = pg.K_SPACE
        self.KEY_EXCLAIM = pg.K_EXCLAIM
        self.KEY_QUOTEDBL = pg.K_QUOTEDBL
        self.KEY_HASH = pg.K_HASH
        self.KEY_PERCENT = pg.K_PERCENT
        self.KEY_DOLLAR = pg.K_DOLLAR
        self.KEY_AMPERSAND = pg.K_AMPERSAND
        self.KEY_QUOTE = pg.K_QUOTE
        self.KEY_LEFTPAREN = pg.K_LEFTPAREN
        self.KEY_RIGHTPAREN = pg.K_RIGHTPAREN
        self.KEY_ASTERISK = pg.K_ASTERISK
        self.KEY_PLUS = pg.K_PLUS
        self.KEY_COMMA = pg.K_COMMA
        self.KEY_MINUS = pg.K_MINUS
        self.KEY_PERIOD = pg.K_PERIOD
        self.KEY_SLASH = pg.K_SLASH
        self.KEY_0 = pg.K_0
        self.KEY_1 = pg.K_1
        self.KEY_2 = pg.K_2
        self.KEY_3 = pg.K_3
        self.KEY_4 = pg.K_4
        self.KEY_5 = pg.K_5
        self.KEY_6 = pg.K_6
        self.KEY_7 = pg.K_7
        self.KEY_8 = pg.K_8
        self.KEY_9 = pg.K_9
        self.KEY_COLON = pg.K_COLON
        self.KEY_SEMICOLON = pg.K_SEMICOLON
        self.KEY_LESS = pg.K_LESS
        self.KEY_EQUALS = pg.K_EQUALS
        self.KEY_GREATER = pg.K_GREATER
        self.KEY_QUESTION = pg.K_QUESTION
        self.KEY_AT = pg.K_AT
        self.KEY_LEFTBRACKET = pg.K_LEFTBRACKET
        self.KEY_BACKSLASH = pg.K_BACKSLASH
        self.KEY_RIGHTBRACKET = pg.K_RIGHTBRACKET
        self.KEY_CARET = pg.K_CARET
        self.KEY_UNDERSCORE = pg.K_UNDERSCORE
        self.KEY_BACKQUOTE = pg.K_BACKQUOTE
        self.KEY_a = pg.K_a
        self.KEY_b = pg.K_b
        self.KEY_c = pg.K_c
        self.KEY_d = pg.K_d
        self.KEY_e = pg.K_e
        self.KEY_f = pg.K_f
        self.KEY_g = pg.K_g
        self.KEY_h = pg.K_h
        self.KEY_i = pg.K_i
        self.KEY_j = pg.K_j
        self.KEY_k = pg.K_k
        self.KEY_l = pg.K_l
        self.KEY_m = pg.K_m
        self.KEY_n = pg.K_n
        self.KEY_o = pg.K_o
        self.KEY_p = pg.K_p
        self.KEY_q = pg.K_q
        self.KEY_r = pg.K_r
        self.KEY_s = pg.K_s
        self.KEY_t = pg.K_t
        self.KEY_u = pg.K_u
        self.KEY_v = pg.K_v
        self.KEY_w = pg.K_w
        self.KEY_x = pg.K_x
        self.KEY_y = pg.K_y
        self.KEY_z = pg.K_z
        self.KEY_CAPSLOCK = pg.K_CAPSLOCK
        self.KEY_F1 = pg.K_F1
        self.KEY_F2 = pg.K_F2
        self.KEY_F3 = pg.K_F3
        self.KEY_F4 = pg.K_F4
        self.KEY_F5 = pg.K_F5
        self.KEY_F6 = pg.K_F6
        self.KEY_F7 = pg.K_F7
        self.KEY_F8 = pg.K_F8
        self.KEY_F9 = pg.K_F9
        self.KEY_F10 = pg.K_F10
        self.KEY_F11 = pg.K_F11
        self.KEY_F12 = pg.K_F12
        self.KEY_PRINTSCREEN = pg.K_PRINT
        self.KEY_SCROLLLOCK = pg.K_SCROLLLOCK
        self.KEY_PAUSE = pg.K_PAUSE
        self.KEY_INSERT = pg.K_INSERT
        self.KEY_HOME = pg.K_HOME
        self.KEY_PAGEUP = pg.K_PAGEUP
        self.KEY_DELETE = pg.K_DELETE
        self.KEY_END = pg.K_END
        self.KEY_PAGEDOWN = pg.K_PAGEDOWN
        self.KEY_RIGHT = pg.K_RIGHT
        self.KEY_LEFT = pg.K_LEFT
        self.KEY_DOWN = pg.K_DOWN
        self.KEY_UP = pg.K_UP
        self.KEY_NUMLOCKCLEAR = pg.K_NUMLOCK
        self.KEY_KP_DIVIDE = pg.K_KP_DIVIDE
        self.KEY_KP_MULTIPLY = pg.K_KP_MULTIPLY
        self.KEY_KP_MINUS = pg.K_KP_MINUS
        self.KEY_KP_PLUS = pg.K_KP_PLUS
        self.KEY_KP_ENTER = pg.K_KP_ENTER
        self.KEY_KP_1 = pg.K_KP1
        self.KEY_KP_2 = pg.K_KP2
        self.KEY_KP_3 = pg.K_KP3
        self.KEY_KP_4 = pg.K_KP4
        self.KEY_KP_5 = pg.K_KP5
        self.KEY_KP_6 = pg.K_KP6
        self.KEY_KP_7 = pg.K_KP7
        self.KEY_KP_8 = pg.K_KP8
        self.KEY_KP_9 = pg.K_KP9
        self.KEY_KP_0 = pg.K_KP0
        self.KEY_KP_PERIOD = pg.K_KP_PERIOD
        self.KEY_POWER = pg.K_POWER
        self.KEY_KP_EQUALS = pg.K_KP_EQUALS
        self.KEY_F13 = pg.K_F13
        self.KEY_F14 = pg.K_F14
        self.KEY_F15 = pg.K_F15
        self.KEY_HELP = pg.K_HELP
        self.KEY_MENU = pg.K_MENU
        self.KEY_SYSREQ = pg.K_SYSREQ
        self.KEY_CLEAR = pg.K_CLEAR
        self.KEY_CURRENCYUNIT = pg.K_CURRENCYUNIT
        self.KEY_CURRENCYSUBUNIT = pg.K_CURRENCYSUBUNIT
        self.KEY_LCTRL = pg.K_LCTRL
        self.KEY_LSHIFT = pg.K_LSHIFT
        self.KEY_LALT = pg.K_LALT
        self.KEY_LGUI = pg.K_LMETA
        self.KEY_RCTRL = pg.K_RCTRL
        self.KEY_RSHIFT = pg.K_RSHIFT
        self.KEY_RALT = pg.K_RALT
        self.KEY_RGUI = pg.K_RMETA
        self.KEY_MODE = pg.K_MODE
        self.KEY_AC_BACK = pg.K_AC_BACK
