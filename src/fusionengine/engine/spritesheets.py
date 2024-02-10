from fusionengine.engine.image import Image


class SpriteSheet:
    def __init__(self, image_path: str, sprite_width: int, sprite_height: int):
        """
        Represents a SpriteSheet containing a grid of frames.

        Args:
            image_path (str): The path to the sprite sheet image file.
            sprite_width (int): Width of each sprite frame.
            sprite_height (int): Height of each sprite frame.
        """
        self.sprite_sheet = Image(image_path, 0, 0, 0, 0)
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.frames = self.get_frames()
        self.width = 0
        self.height = 0

    def get_frames(self) -> list:
        """
        Extract frames from the sprite sheet.

        Returns:
            list: List of Image objects representing individual frames.
        """
        frames = []
        columns = self.sprite_sheet.get_image_size()[0] // self.sprite_width
        rows = self.sprite_sheet.get_image_size()[1] // self.sprite_height

        for row in range(rows):
            for col in range(columns):
                frame = self.extract_frame(col, row)
                frames.append(frame)

        return frames

    def extract_frame(self, col: int, row: int) -> Image:
        """
        Extract a single frame from the sprite sheet.

        Args:
            col (int): Column index of the sprite.
            row (int): Row index of the sprite.

        Returns:
            Image: Image object representing the extracted frame.
        """
        x = col * self.sprite_width
        y = row * self.sprite_height

        frame_surface = self.sprite_sheet.crop(
            x, y, self.sprite_width, self.sprite_height
        )
        frame = Image(frame_surface.image, 0, 0, self.sprite_width, self.sprite_height)
        return frame

    def frame_size(self, width: int, height: int) -> None:
        """
        Set the size of each frame in the sprite sheet.

        Args:
            width (int): Width to set for each frame.
            height (int): Height to set for each frame.
        """
        for frame in self.frames:
            frame.width = width
            frame.height = height

    def frame_pos(self, x: int, y: int) -> None:
        """
        Set the position of each frame in the sprite sheet.

        Args:
            x (int): X position to set for each frame.
            y (int): Y position to set for each frame.
        """
        for frame in self.frames:
            frame.x = x
            frame.y = y
