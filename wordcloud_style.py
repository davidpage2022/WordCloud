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

    def select_colour(self, word, value, word_to_values):
        user_colours = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130),
                   (148, 0, 211)]  # This is a list of RGB codes for the colours of the rainbow
        max_value = max(word_to_values.values())

        # i = 1
        # for value in word_to_values.values():
        #     if value <= max_value / len(user_colours) * i:
        #         red, green, blue = user_colours[len(user_colours) - i]
        #         return f"rgb({red},{green},{blue})"
        #     i += 1

        if value <= max_value / len(user_colours):  # Smallest sized words have the last colour in the list applied
            red, green, blue = user_colours[-1]
            return f"rgb({red},{green},{blue})"
        elif value <= max_value / len(user_colours) * (len(user_colours) - 5):
            red, green, blue = user_colours[-2]
            return f"rgb({red},{green},{blue})"
        elif value <= max_value / len(user_colours) * (len(user_colours) - 4):
            red, green, blue = user_colours[-3]
            return f"rgb({red},{green},{blue})"
        elif value <= max_value / len(user_colours) * (len(user_colours) - 3):
            red, green, blue = user_colours[-4]
            return f"rgb({red},{green},{blue})"
        elif value <= max_value / len(user_colours) * (len(user_colours) - 2):
            red, green, blue = user_colours[-5]
            return f"rgb({red},{green},{blue})"
        elif value <= max_value / len(user_colours) * (len(user_colours) - 1):
            red, green, blue = user_colours[-6]
            return f"rgb({red},{green},{blue})"
        else:  # Largest sized words have the first colour in the list applied
            red, green, blue = user_colours[-7]
            return f"rgb({red},{green},{blue})"
