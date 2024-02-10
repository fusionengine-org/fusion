from fusionengine.engine.window import Window
from fusionengine.engine.shape import Rect
from fusionengine.engine.image import Image
from fusionengine.engine.vector import Vector2D
from fusionengine.engine.animation import Animation
from fusionengine.engine.color import Color


class Node:
    def __init__(self, window: Window, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window = window
        self.frame = 0
        self.to_draw = []

    def get_coord_tuple(self) -> tuple[int, int]:
        """
        Returns the coordinates of the node as a tuple.

        Returns:
            A tuple containing the x and y coordinates of the node.
        """
        return self.x, self.y

    def get_coord_vec2(self) -> Vector2D:
        """
        Returns the coordinates of the node as a Vector2D object.

        Returns:
            Vector2D: The coordinates of the node.
        """
        return Vector2D(self.x, self.y)

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

    def load_image(self, image_path: str) -> None:
        """
        Gives the entity an image and laters draws it on the screen.

        Args:
            image_path (str): The path to the image
        """
        self.to_draw.append(Image(image_path, self.x, self.y, self.width, self.height))

    def load_animation(self, images: tuple | Animation) -> None:
        """
        Loads images that can be later used as a animation.

        Args:
            images (tuple): A tuple of images
        """
        self.to_draw.append(images)

    def load_rect(self, color: Color) -> None:
        """
        Gives the entity a rectangle and later draws it on the screen.

        Args:
            color (tuple): The color of the rectangle
        """
        self.to_draw.append(Rect(self.x, self.y, self.width, self.height, color))

    def update(self):
        """
        Update method for the node.
        This method is called to update the state of the node and to draw everything.
        """
        for draw in self.to_draw:
            if isinstance(draw, tuple):
                draw[self.frame].draw()
            elif isinstance(draw, Animation):
                draw.play()
            else:
                draw.draw()

        self.to_draw = []
