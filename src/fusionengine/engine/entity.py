from fusionengine.engine.window import Window
from fusionengine.engine.image import Image
from fusionengine.engine.shape import Rect
from fusionengine.engine.color import Color
from fusionengine.backend.deprecations import deprecated


class Entity:
    @deprecated("5.0.0", "Entity class")
    def __init__(
        self,
        window: Window,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> None:
        """
        A class that creates a new entity. If set_body isn't called, it will automatically become a StaticBody

        Args:
            window (Window): Your window
            x (int): X position of the entity
            y (int): Y position of the entity
            width (int): Width of the entity
            height (int): Height of the entity
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window = window
        self.gravity = 0
        self.frame = 0
        self.body = None

    def load_image(
        self,
        image_path: str,
    ) -> None:
        """
        Gives the entity an image and laters draws it on the screen.

        Args:
            image_path (str): The path to the image
        """
        self.main_image = Image(image_path, self.x, self.y, self.width, self.height)

    def load_animation(self, images: tuple) -> None:
        """
        Loads images that can be later used as a animation.

        Args:
            images (tuple): A tuple of images
        """
        self.images = images

    def draw_animation(self) -> None:
        """
        Draws the previus loaded images with the current frame that was given.
        """
        self.images[self.frame].draw()

    def draw_image(self) -> None:
        """
        Draws the image previously loaded.
        """
        self.main_image.draw()

    def set_frame(self, frame: int) -> None:
        """
        Sets the frame of the previously loaded images (as a animation).

        Args:
            frame (int): The frame of the animation
        """
        self.frame = frame

    def get_frame(self) -> int:
        """
        Gets the frame of the previously loaded images (as a animation).

        Returns:
            int: The frame of the animation
        """
        return self.frame

    def load_rect(self, color: Color) -> None:
        """
        Gives the entity a rectangle and later draws it on the screen.

        Args:
            color (tuple): The color of the rectangle
        """
        self.main_rect = Rect(self.x, self.y, self.width, self.height, color)

    def draw_rect(self) -> None:
        """
        Draws the rectangle previously loaded.
        """
        self.main_rect.draw()
