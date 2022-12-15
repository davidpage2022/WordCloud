"""Test word cloud tools."""
from PIL import Image, ImageShow

from wordcloud import main
from word import Word

TEXT = """This is a test test string string string."""


def render_to_image(words):
    """Render the word cloud to an image.

    :param words: List of Words in the word cloud."""
    image = Image.new("RGBA", (800, 800), "#000000ff")
    for word in words:
        word.draw_into(image)
    ImageShow.show(image)


def make_physical_words(word_strings):
    """Make physical Words for a list of strings.

    :param: List of strings, each representing a word.
    :return: List of created Words."""
    words = []
    for word_string in word_strings:
        words.append(
            Word(text=word_string, position=(0, 0), angle=0.0, font_size=32))
    return words


def test_word_cloud():
    word_to_occurrence = main()
    print(word_to_occurrence)

    words = make_physical_words(word_to_occurrence.keys())
    for word in words:
        print(word)

    render_to_image(words)


if __name__ == '__main__':
    test_word_cloud()
