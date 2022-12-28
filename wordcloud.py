"""Create word cloud logic program."""
import operator
import string

VALUED_WORDS = ["word", "cloud", "punctuation", "string"]
FACTOR_TO_MULTIPLY_VALUED_WORDS_BY = 5


def word_cloud_logic(source_text, model="occurrence"):
    """Produce a dictionary of words suitable for processing into a word cloud using an occurrence, value, length
    reversed, alphabetical or acronym based model."""
    processed_list = process_string(source_text)
    if model == "occurrence":
        word_to_count = map_word_to_occurrence(processed_list)
    elif model == "value":
        word_to_count = map_word_to_valued_words(processed_list)
    elif model == "length":
        word_to_count = map_word_to_length(processed_list)
    elif model == "reversed":
        word_to_count = create_reversed_words(processed_list)
    else:
        word_to_count = map_word_to_alphabetical_order(processed_list)
    word_to_count = sort_by_value(word_to_count)
    if model == "acronym":
        word_to_count = create_acronym(source_text)
    return word_to_count


def read_file(filename):
    """Read a text file."""
    in_file = open(filename, 'r')
    raw_text = in_file.read()
    in_file.close()
    return raw_text


def process_string(text_to_process):
    """Process the initial string to remove unnecessary punctuation and small-sized words."""
    lower_case_string = text_to_process.lower()
    split_list = lower_case_string.split()
    raw_words_list = [word for word in split_list if len(word) >= 3]  # Will remove minor punctuation errors eg ;;
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
    processed_list = [word for word in fully_stripped_list if len(word) >= 3
                      and word != "and" and word != "the"]
    return processed_list


def map_word_to_occurrence(words):
    """Add list to dictionary with value based on occurrence."""
    word_to_count = {}
    for word in set(words):
        word_to_count[word] = words.count(word)
    return word_to_count


def map_word_to_valued_words(words):
    """Add list to dictionary with value based on nominated keywords."""
    word_to_count = {}
    for word in set(words):
        word_to_count[word] = 1
        if word in VALUED_WORDS:
            word_to_count[word] = (words.count(word) * FACTOR_TO_MULTIPLY_VALUED_WORDS_BY)
    return word_to_count


def map_word_to_length(words):
    """Add list to dictionary with value based on length of word."""
    word_to_count = {}
    for word in set(words):
        word_to_count[word] = len(word)
    return word_to_count


def create_reversed_words(words):
    """Add list to dictionary with words reversed (value of 1 applied to all)."""
    word_to_count = {}
    for word in set(words):
        reversed_word = word[::-1]
        word_to_count[reversed_word] = 1
    return word_to_count


def create_acronym(text_to_process):
    """Creat an acronym using initial letters of words from supplied text."""
    lower_case_string = text_to_process.lower()
    split_list = lower_case_string.split()
    right_stripped_list = []
    for word in split_list:
        while word[-1] in string.punctuation:
            word = word[:-1]
        right_stripped_list.append(word)
    fully_stripped_list = []
    for word in right_stripped_list:
        while word[0] in string.punctuation:
            word = word[1:]
        fully_stripped_list.append(word)
    word_to_count = {}
    acronym = ""
    for word in fully_stripped_list:
        initial = word[0]
        acronym = acronym + initial
    word_to_count[acronym] = 1
    return word_to_count


def map_word_to_alphabetical_order(words):
    """Add list to dictionary with value based on alphabetical order."""
    word_to_count = {}
    words.sort()
    for word in set(words):
        word_to_count[word] = 1
    count = len(word_to_count.values())
    for key in word_to_count:
        word_to_count[key] = count
        count -= 1
    return word_to_count


def sort_by_value(dictionary):
    """Sort dictionary by value in descending order."""
    sorted_dictionary = dict(sorted(dictionary.items(), key=operator.itemgetter(1, 0), reverse=True))
    return sorted_dictionary
