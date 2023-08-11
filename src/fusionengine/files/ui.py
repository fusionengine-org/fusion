from fusionengine.files.imports import *
import fusionengine.files.draw as draw
import fusionengine.files.window as windowfe
import fusionengine.files.shape as shape


class _CustomButton:
    def __init__(
        self, window: windowfe._CustomRenderer, rect: shape._CustomShape, text: str
    ) -> None:
        """A class that creates a new custom button. (Not for the user)"""

        self.manager = window.manager
        self.text = text
        self.x = rect.x
        self.y = rect.y
        self.width = rect.width
        self.height = rect.height

        self.button = gui.elements.UIButton(
            relative_rect=rect.rect, text="Say Hello", manager=self.manager
        )

    def button_pressed(self) -> bool:
        """Returns if the button is pressed."""
        return self.button.check_pressed()


class Button:
    def new_button(
        self, window: windowfe._CustomRenderer, rect: shape._CustomShape, text: str
    ) -> _CustomButton:
        """Creates a new button for your ui."""
        return _CustomButton(window, rect, text)


class Text:
    def print_text(
        self,
        window: windowfe._CustomRenderer,
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
