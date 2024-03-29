"""Test word cloud tools."""

from wordcloud import main
from visual_wordcloud import VisualWordCloud
from wordcloud_style import RandomColourSelector

TEXT = """This is a test test string string string."""
TEST_WORD_TO_OCCURRENCE = {"string": 3, "test": 2, "this": 1, "is": 1, "a": 1}


def test_word_cloud():
    # TODO: Should word_to_occurrence be renamed to word_to_count ?

    word_to_occurrence = main()
    # word_to_occurrence = TEST_WORD_TO_OCCURRENCE
    print(word_to_occurrence)

    colour_selector = RandomColourSelector()
    # colour_selector = RandomColourSelector(background_colour=(255, 0, 0), title_colour=(0, 255, 0))
    word_cloud = VisualWordCloud(word_to_occurrence, colour_selector)
    for visual_word in word_cloud.visual_words:
        print(visual_word)
    word_cloud.render_to_image(title="Title")


if __name__ == '__main__':
    test_word_cloud()
