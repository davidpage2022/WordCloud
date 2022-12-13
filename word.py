"""Word inside a word cloud."""

from PIL import Image, ImageDraw, ImageFont


# TODO: https://stackoverflow.com/questions/45179820/draw-text-on-an-angle-rotated-in-python


class Word:
    """Represents a physical word inside a WordCloud."""

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
        pass

    def draw_into(self, image):
        """Draw the word into a given image."""
        pass

    def __str__(self):
        return f"{self.text} - {self.position} ({self.angle} degrees) - size: {self.font_size}"
