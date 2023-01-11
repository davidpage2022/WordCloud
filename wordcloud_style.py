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


class UserInputBasedSelector(ColourSelector):
    """Apply colour based on a user inputted list."""

    def select_colour(self, word, value, word_to_values):
        user_colours = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130),
                        (148, 0, 211)]  # This is a list of RGB codes for the colours of the rainbow
        maximum_dictionary_value = max(word_to_values.values())
        percentage_range_per_colour = (100 / len(user_colours)) / 100
        if value >= maximum_dictionary_value * percentage_range_per_colour * (len(user_colours) - 1):
            # Largest sized words have the first colour in the list applied
            red = user_colours[0][0]
            green = user_colours[0][1]
            blue = user_colours[0][2]
            return f"rgb({red},{green},{blue})"
        elif value >= maximum_dictionary_value * percentage_range_per_colour * (len(user_colours) - 2):
            red = user_colours[1][0]
            green = user_colours[1][1]
            blue = user_colours[1][2]
            return f"rgb({red},{green},{blue})"
        elif value >= maximum_dictionary_value * percentage_range_per_colour * (len(user_colours) - 3):
            red = user_colours[2][0]
            green = user_colours[2][1]
            blue = user_colours[2][2]
            return f"rgb({red},{green},{blue})"
        elif value >= maximum_dictionary_value * percentage_range_per_colour * (len(user_colours) - 4):
            red = user_colours[3][0]
            green = user_colours[3][1]
            blue = user_colours[3][2]
            return f"rgb({red},{green},{blue})"
        elif value >= maximum_dictionary_value * percentage_range_per_colour * (len(user_colours) - 5):
            red = user_colours[4][0]
            green = user_colours[4][1]
            blue = user_colours[4][2]
            return f"rgb({red},{green},{blue})"
        elif value >= maximum_dictionary_value * percentage_range_per_colour:
            red = user_colours[5][0]
            green = user_colours[5][1]
            blue = user_colours[5][2]
            return f"rgb({red},{green},{blue})"
        else:
            # Smallest sized words have the last colour in the list applied
            red = user_colours[6][0]
            green = user_colours[6][1]
            blue = user_colours[6][2]
            return f"rgb({red},{green},{blue})"
