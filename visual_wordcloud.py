"""Visual arrangement and display of a word cloud."""
from PIL import Image, ImageFont, ImageDraw, ImageShow

from visual_word import VisualWord


class ColourSelector:
    """Handles selection of word colour in the word cloud."""

    def on_begin_draw(self, word_to_values):
        """Handle any set up required before drawing the word cloud.

        Called by a VisualWordCloud before the first word is drawn.
        Override this method in a child class to do any set up.

        :param word_to_values: Dictionary of words to their values."""
        pass

    def select_colour(self, word, value, word_to_values):
        """Return the colour to use for a word in the word cloud.

        The default is white text.
        Override this method in a child class to customise the colour.

        :param word: Word string.
        :param value: Value of the word.
        This is typically the number of times the word occurred in the original text.
        :param word_to_values: Dictionary of words to their values.
        :returns: Colour to use for the word as a string. For the string format see Pillow documentation:
        https://pillow.readthedocs.io/en/stable/reference/ImageColor.html"""
        return "white"

    def on_end_draw(self):
        """Handle any clean up required after drawing the word cloud.

        Called by a VisualWordCloud after the last word is drawn.
        Override this method in a child class to do any clean up."""
        pass


class VisualWordCloud:
    """Visual representation of a word cloud"""
    MIN_FONT_SIZE = 12
    MAX_FONT_SIZE = 70
    FONT_SIZE_EXPONENT = 1.2

    def __init__(self, word_to_values, colour_selector=ColourSelector()):
        """Construct a visual word cloud.

        :param word_to_values: Dictionary of words to their occurrence.
        :param colour_selector: Selector for choosing word colours."""
        self.colour_selector = colour_selector
        self.word_to_values = word_to_values
        self.word_to_weight = self._calculate_weights()
        self.visual_words = self._make_words()

    def _calculate_weights(self):
        """Calculate relative weights of words based on their occurrences.
        The sum of all weights equals 1.

        :returns: Dictionary of words to their weights."""
        word_to_weight = {}
        total_word_count = sum(self.word_to_values.values())
        for word, count in self.word_to_values.items():
            weight = count / total_word_count
            word_to_weight[word] = weight
        return word_to_weight

    def _make_words(self):
        """Create visual word objects and place them in random positions.

        :returns: List of created VisualWord objects."""
        self.colour_selector.on_begin_draw(self.word_to_values)
        visual_words = []
        for word, count in self.word_to_values.items():
            weight = self.word_to_weight[word]
            visual_words.append(
                VisualWord(text=word, position=(0, 0), angle=0.0,
                           font_size=self._determine_font_size(word, self.FONT_SIZE_EXPONENT),
                           font_colour=self.colour_selector.select_colour(word, count, self.word_to_values)))
        self.colour_selector.on_end_draw()
        return visual_words

    def _determine_font_size(self, word, bias=1.0):
        """Determine a suitable font size for a word based on the relative weights of word occurrences.

        :param bias: Exponent used to bias towards having smaller or larger words.
        :returns: The font size determined, in pixels."""
        max_weight = max(self.word_to_weight.values())
        weight = (self.word_to_weight[word] / max_weight) ** bias
        font_size_range = self.MAX_FONT_SIZE - self.MIN_FONT_SIZE
        font_size = int(self.MIN_FONT_SIZE + weight * font_size_range)
        return font_size

    def render_to_image(self, title=""):
        """Render the word cloud to a temporary image and show it using default system viewer.

        :param title: Optional title to display at the top-left of the image."""
        image = Image.new("RGBA", (800, 800), "#000000ff")
        for visual_word in self.visual_words:
            visual_word.draw_into(image)
        self._draw_text_into(image, title, (20, 20), 26, "#666666")
        ImageShow.show(image)

    @staticmethod
    def _draw_text_into(image, text, position, font_size, colour="white"):
        """Draw text into an image."""
        font = ImageFont.truetype("arial.ttf", font_size)

        # Draw text to mask.
        mask = Image.new('L', image.size)
        mask_drawer = ImageDraw.Draw(mask)
        mask_drawer.text(position, text, 255, font)

        # Draw into image.
        color_image = Image.new('RGBA', image.size, colour)
        image.paste(color_image, mask)
