"""Test word cloud tools."""
from wordcloud import read_file
from wordcloud import word_cloud_logic
from visual_wordcloud import VisualWordCloud

TEST_STRING = "Sometimes unusual richness presents readily in sunset experiences."
# TEST_STRING = "This is a test test string string string."
TEST_FILE = "initial_text.txt"
TEST_MODEL = "acronym"  # Model options are "occurrence", "value", "length", "reversed", "alphabetical" and "acronym.
TEST_WORD_TO_OCCURRENCE = {"string": 3, "test": 2, "this": 1, "is": 1, "a": 1}


def test_word_cloud():
    """Test word cloud logic tools."""
    text = TEST_STRING
    # text = read_file(TEST_FILE)
    word_to_count = word_cloud_logic(text, TEST_MODEL)
    # word_to_count = TEST_WORD_TO_COUNT
    print(word_to_count)

    word_cloud = VisualWordCloud(word_to_count)
    for visual_word in word_cloud.visual_words:
        print(visual_word)
    word_cloud.render_to_image(title=f"{TEST_MODEL.title()} Model")


if __name__ == '__main__':
    test_word_cloud()
