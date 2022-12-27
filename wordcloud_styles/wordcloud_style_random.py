"""Select word cloud colour randomly."""
from random import randint

from wordcloud_styles.wordcloud_style import WordCloudStyle


class WordCloudStyleRandom(WordCloudStyle):
    """Select word cloud colour randomly."""

    def select_word_colour(self, word, value, weight):  # Overrides WordCloudStyle.select_word_colour()
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        return f"rgb({red},{green},{blue})"
