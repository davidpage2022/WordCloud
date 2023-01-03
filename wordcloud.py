"""Create word cloud logic program."""
import operator
import string

VALUED_WORDS = ["test"]
VALUED_CHARACTERS = ["s"]
FACTOR_TO_MULTIPLY_VALUED_ITEMS_BY = 5


def word_cloud_logic(source_text, model="occurrence"):
    """Produce a dictionary of words suitable for processing into a word cloud using the specified model.

    Available models:
    "occurrence": Creates a dictionary based on occurrence of words within list.
    "valued-words": Creates a dictionary based on value applied to nominated keywords.
    "valued-characters": Creates a dictionary based on value applied to nominated initial letter of words.
    "length": Creates a dictionary based on length of words within list.
    "reversed": Creates a dictionary of words in their reversed order (value of 1 applied to all).
    "phrase":  Creates a dictionary of phrases with value based inversely on length.
    "alphabetical": Creates a dictionary based on alphabetical order of words within list.
    "multiple-choice":  Creates a dictionary of multiple choice options with value based on number of responses.
    "acronym": Creates a new word from the initial letters of words within the supplied text.
    """

    processed_list = process_string(source_text)
    if model == "occurrence":
        word_to_count = map_word_to_occurrence(processed_list)
    elif model == "valued-words":
        word_to_count = map_word_to_valued_words(processed_list)
    elif model == "valued-characters":
        word_to_count = map_word_to_valued_characters(processed_list)
    elif model == "length":
        word_to_count = map_word_to_length(processed_list)
    elif model == "reversed":
        word_to_count = create_reversed_words(processed_list)
    elif model == "phrase":
        word_to_count = map_phrase_to_length(source_text)
    elif model == "multiple-choice":
        word_to_count = process_multiple_choice(source_text)
    else:
        word_to_count = map_word_to_alphabetical_order(processed_list)  # alphabetical model
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
    """Process the initial string to a suitable format for dictionary creation."""
    lower_case_string = text_to_process.lower()
    split_list = lower_case_string.split()
    fully_stripped_list = strip_list(split_list)
    processed_list = [word for word in fully_stripped_list if len(word) >= 3
                      and word != "and" and word != "the"]
    return processed_list


def strip_list(split_list):
    """Strip unnecessary punctuation and whitespace from ends of string."""
    right_stripped_list = []
    for unit in split_list:
        while len(unit) > 0 and unit[-1].strip() in string.punctuation:
            unit = unit[:-1]
        right_stripped_list.append(unit)
    right_stripped_list = [item for item in right_stripped_list if item != ""]
    fully_stripped_list = []
    for unit in right_stripped_list:
        while len(unit) > 0 and unit[0].strip() in string.punctuation:
            unit = unit[1:]
        fully_stripped_list.append(unit)
    return fully_stripped_list


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
            word_to_count[word] = (words.count(word) * FACTOR_TO_MULTIPLY_VALUED_ITEMS_BY)
    return word_to_count


def map_word_to_valued_characters(words):
    """Add list to dictionary with value based on nominated characters."""
    word_to_count = {}
    for word in set(words):
        word_to_count[word] = 1
        if word[0] in VALUED_CHARACTERS:
            word_to_count[word] = (words.count(word) * FACTOR_TO_MULTIPLY_VALUED_ITEMS_BY)
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


def map_phrase_to_length(text_to_process):
    """Add list of phrases to dictionary with value based inversely on length."""
    lower_case_string = text_to_process.lower()
    split_list = lower_case_string.split(',')
    fully_stripped_phrase = strip_list(split_list)
    print(fully_stripped_phrase)
    sorted_list = sorted(fully_stripped_phrase, key=len)
    word_to_count = {}
    for phrase in set(sorted_list):
        word_to_count[phrase] = (len(sorted_list[-1]) - len(phrase))
    return word_to_count


def process_multiple_choice(text_to_process):
    """Add multiple choice options to dictionary with value based on number of responses."""
    lower_case_string = text_to_process.lower()
    split_list = lower_case_string.split(',')
    fully_stripped_phrase = strip_list(split_list)
    half_length_of_list = int(len(fully_stripped_phrase) / 2)
    options = fully_stripped_phrase[:half_length_of_list]
    string_responses = fully_stripped_phrase[half_length_of_list:]
    integer_responses = []
    for number in string_responses:
        number = int(number)
        integer_responses.append(number)
    word_to_count = dict(zip(options, integer_responses))
    return word_to_count


def map_word_to_alphabetical_order(words):
    """Add list to dictionary with value based on alphabetical order."""
    word_to_count = {}
    words.sort()
    for word in words:
        word_to_count[word] = 1
    count = len(word_to_count.values())
    for key in word_to_count:
        word_to_count[key] = count
        count -= 1
    return word_to_count


def create_acronym(text_to_process):
    """Creat an acronym using initial letters of words from supplied text."""
    lower_case_string = text_to_process.lower()
    split_list = lower_case_string.split()
    fully_stripped_list = strip_list(split_list)
    word_to_count = {}
    acronym = ""
    for word in fully_stripped_list:
        initial = word[0]
        acronym = acronym + initial
    word_to_count[acronym] = 1
    return word_to_count


def sort_by_value(dictionary):
    """Sort dictionary by value in descending order."""
    sorted_dictionary = dict(sorted(dictionary.items(), key=operator.itemgetter(1, 0), reverse=True))
    return sorted_dictionary
