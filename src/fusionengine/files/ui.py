from fusionengine.files.imports import *
import fusionengine.files.draw as draw
import fusionengine.files.window as windowfe


class _CustomButton:
    def __init__(
        self,
        window: window._CustomRenderer,
        text: str,
        x: int,
        y: int,
        width: int,
        height: int,
        font_path: str,
        font_size_input: int,
        center: int,
        color_input: tuple,
    ) -> None:
        """A class that creates a new custom button. (Not for the user)"""
        self.window = window
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_path = font_path
        self.font_size_input = font_size_input
        self.center = center
        self.color = color_input
        self.is_pressed = False

        if self.font_size_input == "default":
            font_size = 30  # Change the default font size to a reasonable value
        else:
            font_size = font_size_input

        draw.Draw().draw_rect(window, x, y, width, height, self.color)

        self.font = pg.font.Font(font_path, font_size)
        self.text_surface = self.font.render(text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect(center=(x + width // 2, y + height // 2))  # Center the text

    def _handle_event(self) -> bool:
        """Handles the event of the mouse."""
        return pg.mouse.get_pressed()[0] and self.is_mouse_over_button()

    def is_mouse_over_button(self) -> bool:
        """Checks if the mouse is over the button."""
        mouse_x, mouse_y = pg.mouse.get_pos()
        return (
            self.x <= mouse_x <= self.x + self.width and
            self.y <= mouse_y <= self.y + self.height
        )

    def is_button_pressed(self) -> bool:
        """Returns if the button is pressed."""
        return self._handle_event()

    def set_color(self, color: tuple) -> None:
        """Sets the color of the button's background."""
        self.color = color

    def button_pressed(self, func: callable) -> None:
        """Custom decorator function that executes a function when the button is pressed."""
        if self.is_button_pressed() and callable(func):
            func()

class Button:
    def new_button(
        self,
        window: window._CustomRenderer,
        text: str,
        x: int,
        y: int,
        width: int,
        height: int,
        font_path: str,
        font_size_input: int,
        center: int,
        color: tuple,
    ) -> _CustomButton:
        """Creates a new button for your ui."""
        return _CustomButton(
            window, text, x, y, width, height, font_path, font_size_input, center, color
        )

class Text:
    def print_text(
        self,
        window: window._CustomRenderer,
        text: str,
        x: int,
        y: int,
        width: int,
        height: int,
        font_path: str,
        font_size: int,
        color: tuple,
    ) -> None:
        """Prints text on the screen."""
        font = pg.font.Font(font_path, font_size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        window.window.blit(text_surface, text_rect)

class UI:
    def __init__(self) -> None:
        """A class that creates a new ui."""
        self.button = Button()
        self.text = Text()