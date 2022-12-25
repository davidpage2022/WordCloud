"""Test word cloud tools."""
from wordcloud import main
from visual_wordcloud import VisualWordCloud

# TEXT = "This is a test test string string string."
TEXT = "initial_text.txt"
TEST_WORD_TO_OCCURRENCE = {"string": 3, "test": 2, "this": 1, "is": 1, "a": 1}


def test_word_cloud():

    word_to_count = main(TEXT, "alphabetical")
    # word_to_count = TEST_WORD_TO_OCCURRENCE
    print(word_to_count)

    word_cloud = VisualWordCloud(word_to_count)
    for visual_word in word_cloud.visual_words:
        print(visual_word)
    word_cloud.render_to_image()


if __name__ == '__main__':
    test_word_cloud()
