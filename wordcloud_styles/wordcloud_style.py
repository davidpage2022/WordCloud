"""Tools for customising the appearance of the word cloud."""


class WordCloudStyle:
    """Describes visual appearance of a word cloud."""

    def select_word_colour(self, word, value, weight):
        """Return the colour to use for a word in the word cloud.

        The default style is simply white text.
        Override this method in a child class to customise the colour.

        :param word: Word string.
        :param value: Value of the word.
        This is usually the number of times the word occurred in the original text.
        :param weight: Value of the word divided by the sum of all values in the word cloud.
        :returns: Colour to use for the word as a string. For the string format see Pillow documentation:
        https://pillow.readthedocs.io/en/stable/reference/ImageColor.html"""
        return "white"
