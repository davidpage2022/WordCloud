TEST_STRING = "This is a test test string string string"


def main():
    """Turn string into data suitable for a word cloud."""
    words = split_string(TEST_STRING)
    word_to_occurrence = {}
    dictionary = add_to_dictionary(words, word_to_occurrence)
    print(dictionary)  # TODO Remove this line
    return dictionary


def split_string(string):
    """Split string into separate words."""
    text = string.split()
    return text


def add_to_dictionary(text, dictionary):
    """Add words and word count to a dictionary."""
    for item in text:
        dictionary[item] = text.count(item)
    return dictionary


main()
