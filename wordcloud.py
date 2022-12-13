"""Tools to create a word cloud from text."""
import string
from operator import itemgetter


class WordCloud:
    """Spatial visualisation for highlighting the most frequently occurring words in text."""

    def __init__(self, text, excluded_words=None, min_length=0, max_words=None):
        """Construct a word cloud.

        :param text: Text string to visualise.
        :param excluded_words: List of words to ignore (all lowercase).
        :param min_length: Minimum length of words included in the visualisation.
        :param max_words: Maximum number of words to visualise. If None set no limit.
        """
        if excluded_words is None:  # Needed to prevent "mutable default".
            excluded_words = []
        words = self._extract_words(text)
        self._words = self._filter_words(words, excluded_words, min_length, max_words)
        self.word_to_count = self._count_word_occurrences(self._words)

    @staticmethod
    def load_text_from_file(filename):
        """Load text from a file."""
        with open(filename, encoding="UTF-8") as in_file:
            return in_file.read()

    @staticmethod
    def _extract_words(text):
        """Extract a list of words from text, ignoring punctuation and case."""
        text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation.
        words = text.lower().split()
        return words

    @staticmethod
    def _filter_words(words, excluded_words, min_length, max_words):
        """Filter a list of words to exclude excluded_words,
         any word shorter than min_length and limit list to max_words (if not None)."""
        if excluded_words:
            for word in excluded_words:
                words.remove(word)
        if min_length > 0:
            words = [word for word in words if len(word) >= min_length]
        if max_words is None:
            return words
        else:
            return words[:max_words + 1]

    @staticmethod
    def _count_word_occurrences(words):
        """Count the number of times a word occurs in a list of words.
        :returns: Dictionary of words to their number of occurrences,
        sorted from highest to lowest occurrence, then alphabetical."""
        word_to_count = {}
        for word in words:
            if word in word_to_count:
                word_to_count[word] += 1
            else:
                word_to_count[word] = 1
        return {word: count for word, count in
                sorted(
                    sorted(word_to_count.items(), key=itemgetter(0)),
                    key=itemgetter(1), reverse=True)}

    def render_to_image(self, filename, open_after=False):
        """Render the word cloud to an image.

        :param filename: File path to write the image to.
        :param open_after: Should we open the image with default image viewer."""
        print("Rendering...")
        pass  # TODO: Implement
