"""Visual arrangement and display of a word cloud."""
from PIL import Image, ImageShow

from visual_word import VisualWord


class VisualWordCloud:
    """Visual representation of a word cloud"""

    def __init__(self, word_to_occurrence):
        """Construct a visual word cloud.

        :param word_to_occurrence: Dictionary of words to their occurrence."""
        self.word_to_occurrence = word_to_occurrence
        self.visual_words = self.make_words()

    def make_words(self):
        """Create visual word objects and place them in random positions.

        :returns: List of created VisualWord objects."""
        visual_words = []
        for word in self.word_to_occurrence.keys():
            visual_words.append(
                VisualWord(text=word, position=(0, 0), angle=0.0, font_size=32))
        return visual_words

    def render_to_image(self):
        """Render the word cloud to a temporary image and show it using default system viewer."""
        image = Image.new("RGBA", (800, 800), "#000000ff")
        for visual_word in self.visual_words:
            visual_word.draw_into(image)
        ImageShow.show(image)
