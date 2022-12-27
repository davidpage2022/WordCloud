"""Create word cloud logic program."""
import operator
import string

VALUED_WORDS = ["word", "cloud", "punctuation"]
FACTOR_TO_MULTIPLY_VALUE_WORDS_BY = 5


def word_cloud_logic(source_text, model="occurrence"):
    """Produce a dictionary of words suitable for processing into a word cloud using an occurrence, value, length or
    alphabetical based model."""
    processed_list = process_string(source_text)
    if model == "occurrence":
        word_to_count = create_dictionary_based_on_word_occurrence(processed_list)
    elif model == "value":
        word_to_count = create_dictionary_based_on_valued_words(processed_list)
    elif model == "length":
        word_to_count = create_dictionary_based_on_word_length(processed_list)
    elif model == "reversed":
        word_to_count = create_dictionary_based_on_reversal(processed_list)
    else:
        word_to_count = create_dictionary_based_on_alphabetical_order(processed_list)
    word_to_count = sort_by_value(word_to_count)
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


def create_dictionary_based_on_word_occurrence(list_of_words):
    """Add list to dictionary with value based on occurrence."""
    word_to_count = {}
    for word in list_of_words:
        word_to_count[word] = list_of_words.count(word)
    return word_to_count


def create_dictionary_based_on_valued_words(list_of_words):
    """Add list to dictionary with value based on nominated keywords."""
    word_to_count = {}
    for word in list_of_words:
        word_to_count[word] = 1
        if word in VALUED_WORDS:
            word_to_count[word] = (list_of_words.count(word) * FACTOR_TO_MULTIPLY_VALUE_WORDS_BY)
    return word_to_count


def create_dictionary_based_on_word_length(list_of_words):
    """Add list to dictionary with value based on length of word."""
    word_to_count = {}
    for word in list_of_words:
        word_to_count[word] = len(word)
    return word_to_count


def create_dictionary_based_on_reversal(list_of_words):
    word_to_count = {}
    for word in list_of_words:
        reversed_word = word[::-1]
        word_to_count[reversed_word] = 1
    return word_to_count


def create_dictionary_based_on_alphabetical_order(list_of_words):
    """Add list to dictionary with value based on alphabetical order."""
    word_to_count = {}
    list_of_words.sort()
    for word in list_of_words:
        word_to_count[word] = 1
    count = len(word_to_count.values())
    for key in word_to_count:
        word_to_count[key] = count
        count -= 1
    return word_to_count


# def insert_name(dictionary, name):
#     """Insert name of model into dictionary (will appear as the last item)."""
#     maximum_value = (max(dictionary.values()) + 10)
#     dictionary[name] = maximum_value
#     return dictionary


def sort_by_value(dictionary):
    """Sort dictionary by value in descending order."""
    sorted_dictionary = dict(sorted(dictionary.items(), key=operator.itemgetter(1, 0), reverse=True))
    return sorted_dictionary
