"""Physical word inside a word cloud."""
import random

from PIL import Image, ImageFont, ImageDraw


class VisualWord:
    """Represents a physical word inside a WordCloud.
    A Word has a physical shape and visual representation."""

    def __init__(self, text, position, angle, font_size):
        """Construct a word.

        :param text: Text of the word.
        :param position: Position inside the word cloud as an (x, y) tuple.
        Coordinates are in the range 0-1, where (0,0) is upper-left corner.
        :param angle: Angle in degrees to rotate the word clockwise.
        :param font_size: Size of the font in pixels."""
        self.text = text
        self.position = position
        self.angle = angle
        self.font_size = font_size

    def check_is_overlapping(self, other_word) -> bool:
        """Determine if another word overlaps with this word."""
        pass  # TODO

    def draw_into(self, image):
        """Draw the word into a given image."""
        text_position = (
            image.size[0] / 2 + random.randint(-200, 200),
            image.size[1] / 2 + random.randint(-200, 200))
        font = ImageFont.truetype("arial.ttf", self.font_size)  # TODO: Cache font.

        # Draw text to mask.
        mask = Image.new('L', image.size)
        mask_drawer = ImageDraw.Draw(mask)
        mask_drawer.text(text_position, self.text, 255, font)

        # Draw into image.
        color_image = Image.new('RGBA', image.size, "#ffffffff")
        image.paste(color_image, mask)

        # TODO: Add rotation support.
        # See https://stackoverflow.com/questions/45179820/draw-text-on-an-angle-rotated-in-python

    def __str__(self):
        return f"{self.text} - {self.position} ({self.angle} degrees) - size: {self.font_size}"
