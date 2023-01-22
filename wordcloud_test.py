"""Test word cloud logic tools."""

from wordcloud import read_file
from wordcloud import word_cloud_logic
from visual_wordcloud import VisualWordCloud
from wordcloud_style import RandomColourSelector
from wordcloud_style import QuantizedColourSelector

# Model options are "occurrence", "valued-words", "valued-characters", "length", "reversed",
# "phrase", "alphabetical" "multiple-choice" and "acronym".
MODEL = "occurrence"

# For testing all models except for phrase & acronym
# TEST_STRING_1 = "$%&*@&&&&### @@@ This% :is a $test$ test    +string string+ string."
TEST_STRING_1 = "red red red red red red red orange orange orange orange orange orange yellow yellow yellow yellow " \
                "yellow green green green green blue blue blue indigo indigo violet"

# For testing phrase model
TEST_STRING_2 = "$%&*@?><&&& %%% &One cat* ,  $$$Two big dogs<<< *   , &&Three hungry yellow chicks**, *** Four&&&"

# For testing acronym model
TEST_STRING_3 = "$%&*@&&&&### @@@ ?People #really$ only    get &ready& after making milkshakes in nice glasses. $%&*@"

# For testing multiple-choice model
MULTIPLE_CHOICE_OPTIONS = "$%&*@&&&&### @@@ %Dictionaries are fun   , &Lists are fun* ,   &@@*Sets are fun, $%&*@ " \
                          "Classes are really fun, "
MULTIPLE_CHOICE_RESPONSES = "5, 10, 3, 20"

# For testing a string found in a text file
TEST_FILE = "initial_text.txt"


# TEST_WORD_TO_OCCURRENCE = {"string": 3, "test": 2, "this": 1, "is": 1, "a": 1}


def test_word_cloud():
    """Test word cloud logic tools."""
    if MODEL == "occurrence" or MODEL == "valued-words" or MODEL == "valued-characters" or MODEL == "length" or \
            MODEL == "reversed" or MODEL == "alphabetical":
        text = TEST_STRING_1
        # text = read_file(TEST_FILE)
    elif MODEL == "phrase":
        text = TEST_STRING_2
    elif MODEL == "multiple-choice":
        text = MULTIPLE_CHOICE_OPTIONS + MULTIPLE_CHOICE_RESPONSES
    else:  # For testing acronym model
        text = TEST_STRING_3
    word_to_count = word_cloud_logic(text, MODEL)
    # word_to_count = TEST_WORD_TO_COUNT
    print(word_to_count)

    colours = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130),
               (148, 0, 211)]  # This is a list of RGB codes for the colours of the rainbow
    # colours = []  # Empty list to test select_colour() method
    colour_selector = QuantizedColourSelector(colours)
    word_cloud = VisualWordCloud(word_to_count, colour_selector)
    for visual_word in word_cloud.visual_words:
        print(visual_word)
    word_cloud.render_to_image(title=f"Page's Panoramic Paragraph\n({MODEL.title()} Model)")


if __name__ == '__main__':
    test_word_cloud()
