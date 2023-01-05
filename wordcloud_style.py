"""Tools to customize the appearance of the word cloud."""
from random import randint

from visual_wordcloud import ColourSelector


class RandomColourSelector(ColourSelector):
    """Select word cloud colour randomly."""

    def select_colour(self, word, value, word_to_values):
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        return f"rgb({red},{green},{blue})"
