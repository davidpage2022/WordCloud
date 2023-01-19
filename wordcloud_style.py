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


class QuantizedColourSelector(ColourSelector):
    """Apply colour based on a user provided list."""

    def __init__(self, colour_list, max_value):
        self.colour_list = colour_list
        self.max_value = max_value

    def on_begin_draw(self, word_to_values):
        # Docstring from parent class:
        """Handle any set up required before drawing the word cloud.

        Called by a VisualWordCloud before the first word is drawn.
        Override this method in a child class to do any set up.

        :param word_to_values: Dictionary of words to their values."""
        self.max_value = max(word_to_values.values())

    def select_colour(self, word, value, word_to_values):

        # max_value = max(word_to_values.values())

        # i = 1
        # for value in word_to_values.values():
        #     if value <= max_value / len(user_colours) * i:
        #         red, green, blue = user_colours[len(user_colours) - i]
        #         return f"rgb({red},{green},{blue})"
        #     i += 1

        if value <= self.max_value / len(self.colour_list):  # Smallest sized words have the last colour in the list applied
            red, green, blue = self.colour_list[-1]
            return f"rgb({red},{green},{blue})"
        elif value <= self.max_value / len(self.colour_list) * (len(self.colour_list) - 5):
            red, green, blue = self.colour_list[-2]
            return f"rgb({red},{green},{blue})"
        elif value <= self.max_value / len(self.colour_list) * (len(self.colour_list) - 4):
            red, green, blue = self.colour_list[-3]
            return f"rgb({red},{green},{blue})"
        elif value <= self.max_value / len(self.colour_list) * (len(self.colour_list) - 3):
            red, green, blue = self.colour_list[-4]
            return f"rgb({red},{green},{blue})"
        elif value <= self.max_value / len(self.colour_list) * (len(self.colour_list) - 2):
            red, green, blue = self.colour_list[-5]
            return f"rgb({red},{green},{blue})"
        elif value <= self.max_value / len(self.colour_list) * (len(self.colour_list) - 1):
            red, green, blue = self.colour_list[-6]
            return f"rgb({red},{green},{blue})"
        else:  # Largest sized words have the first colour in the list applied
            red, green, blue = self.colour_list[-7]
            return f"rgb({red},{green},{blue})"
