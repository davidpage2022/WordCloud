"""Test word cloud logic tools."""

from random import randint
from wordcloud import read_file
from wordcloud import word_cloud_logic
from visual_wordcloud import VisualWordCloud
from wordcloud_style import RandomColourSelector
from wordcloud_style import QuantizedColourSelector

# Model options are "occurrence", "valued-words", "valued-characters", "length", "reversed",
# "phrase", "alphabetical" "multiple-choice" and "acronym".
MODEL = "occurrence"
# COLOUR_MODEL options are "rainbow", "defined-number" and "graduated"
COLOUR_MODEL = "graduated"

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

    colour_selector = QuantizedColourSelector(test_wordcloud_usercolour())
    # colour_selector = RandomColourSelector(background_colour=(0, 183, 235), title_colour=(255, 255, 255))

    word_cloud = VisualWordCloud(word_to_count, colour_selector)
    for visual_word in word_cloud.visual_words:
        print(visual_word)
    word_cloud.render_to_image(title=f"Page's Panoramic Paragraph\n({MODEL.title()} Model)")


def test_wordcloud_usercolour():
    if COLOUR_MODEL == "rainbow":  # Provides a list of RGB codes for the colours of the rainbow
        colours = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130),
                   (148, 0, 211)]
        return colours
    elif COLOUR_MODEL == "defined-number":  # Provides a list of random length of random colours
        number_of_colours = randint(3, 5)
        colours = []
        for i in range(number_of_colours):
            red = randint(0, 255)
            green = randint(0, 255)
            blue = randint(0, 255)
            colour = red, green, blue
            colours.append(colour)
        return colours
    elif COLOUR_MODEL == "graduated":  # Provides a list of graduated colours of random number of shades
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        start_colour = red, green, blue
        steps = randint(3, 10)
        red_step = int((255 - red) / steps)
        green_step = int((255 - green) / steps)
        blue_step = int((255 - blue) / steps)
        colours = [start_colour]
        for i in range(steps):
            red = red + red_step
            green = green + green_step
            blue = blue + blue_step
            colour = (red, green, blue)
            colours.append(colour)
        return colours


if __name__ == '__main__':
    test_word_cloud()
