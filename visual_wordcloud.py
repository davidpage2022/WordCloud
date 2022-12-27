"""Visual arrangement and display of a word cloud."""
from PIL import Image, ImageFont, ImageDraw, ImageShow

from visual_word import VisualWord
from wordcloud_styles.wordcloud_style import WordCloudStyle


class VisualWordCloud:
    """Visual representation of a word cloud"""
    MIN_FONT_SIZE = 12
    MAX_FONT_SIZE = 70
    FONT_SIZE_EXPONENT = 1.2

    def __init__(self, word_to_occurrence, style=WordCloudStyle()):
        """Construct a visual word cloud.

        :param word_to_occurrence: Dictionary of words to their occurrence.
        :param style: Custom style to use for displaying the word cloud."""
        self.style = style
        self.word_to_occurrence = word_to_occurrence
        self.word_to_weight = self._calculate_weights()
        self.visual_words = self._make_words()

    def _calculate_weights(self):
        """Calculate relative weights of words based on their occurrences.
        The sum of all weights equals 1.

        :returns: Dictionary of words to their weights."""
        word_to_weight = {}
        total_word_count = sum(self.word_to_occurrence.values())
        for word, count in self.word_to_occurrence.items():
            weight = count / total_word_count
            word_to_weight[word] = weight
        return word_to_weight

    def _make_words(self):
        """Create visual word objects and place them in random positions.

        :returns: List of created VisualWord objects."""
        visual_words = []
        for word, count in self.word_to_occurrence.items():
            weight = self.word_to_weight[word]
            visual_words.append(
                VisualWord(text=word, position=(0, 0), angle=0.0,
                           font_size=self._determine_font_size(word, self.FONT_SIZE_EXPONENT),
                           font_colour=self.style.select_word_colour(word, count, weight)))
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
