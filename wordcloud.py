import string

TEST_STRING = "This and the this is a very tricky string tricky-string to use in a " \
              "word &word #word% cloud cloud! cloud."


def main():
    """Produce word cloud words and test function in use."""
    word_cloud_words = make_word_cloud_words(TEST_STRING)
    assert word_cloud_words == {'this': 2, 'very': 1, 'tricky': 1, 'string': 1, 'tricky-string': 1,
                                'use': 1, 'word': 3, 'cloud': 3}
    return word_cloud_words


def make_word_cloud_words(initial_string):
    """Turn initial string into words suitable for a word cloud."""
    lower_case_string = initial_string.lower()
    raw_words_list = lower_case_string.split()
    right_stripped_list = []
    for word in raw_words_list:
        while word[-1] in string.punctuation:
            word = word[:-1]
        right_stripped_list.append(word)
    fully_stripped_list = []
    for word in right_stripped_list:
        while word[0] in string.punctuation:
            word = word[1:]
        fully_stripped_list.append(word)
    long_word_list = [word for word in fully_stripped_list if len(word) >= 3
                      and word != "and" and word != "the"]
    word_to_occurrence = {}
    for word in long_word_list:
        word_to_occurrence[word] = long_word_list.count(word)
    return word_to_occurrence


main()
