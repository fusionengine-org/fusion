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
        font_path: str,
        font_size: int,
        color: tuple,
    ) -> None:
        """Prints text on the screen."""

        if os.path.exists(font_path):
            font = pg.font.Font(font_path, font_size)
        else:
            font = pg.font.SysFont(font_path, font_size)

        txtsurf = font.render(text, True, color)

        window.window.blit(txtsurf, (x, y))


class UI:
    def __init__(self) -> None:
        """A class that creates a new ui."""
        self.button = Button()
        self.text = Text()
