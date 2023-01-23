"""Tools to customize the appearance of the word cloud."""
from random import randint

from visual_wordcloud import ColourSelector


class RandomColourSelector(ColourSelector):
    """Select word cloud colour randomly."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def select_colour(self, word, value, word_to_values):
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        return f"rgb({red},{green},{blue})"


class QuantizedColourSelector(ColourSelector):
    """Apply colour based on a user provided list."""

    def __init__(self, colour_list):
        super().__init__(background_colour=(255, 255, 255), title_colour=(0, 0, 0))
        self.colour_list = colour_list
        self.max_value = 0

    def on_begin_draw(self, word_to_values):
        # Docstring from parent class:
        """Handle any set up required before drawing the word cloud.

        Called by a VisualWordCloud before the first word is drawn.
        Override this method in a child class to do any set up.

        :param word_to_values: Dictionary of words to their values."""
        self.max_value = max(word_to_values.values())

    def select_colour(self, word, value, word_to_values):
        assert len(self.colour_list) > 0

        for i in range(len(self.colour_list)):
            if value <= i + 1:
                return self.colour_list[len(self.colour_list) - 1 - i]
        return self.colour_list[-1]

        # Erica's original version with default of white:
        # if self.colour_list:
        #     i = 1
        #     for colour in self.colour_list:
        #         if value <= self.max_value / len(self.colour_list) * i:
        #             return self.colour_list[len(self.colour_list) - i]
        #         i += 1
        #     return self.colour_list[-1]
        # red = 255
        # green = 255
        # blue = 255
        # return f"rgb({red},{green},{blue})"
