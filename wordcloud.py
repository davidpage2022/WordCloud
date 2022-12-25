import operator
import string

WORDS_WITH_VALUE = ["word", "cloud", "punctuation"]


def main(source_text, model_selection="occurrence"):
    """Produce words suitable for processing into a word cloud using random model selection."""
    raw_text = read_file(source_text)
    processed_list = process_string(raw_text)
    if model_selection == "occurrence":  # Creates a dictionary based on occurrence of words within list
        word_to_count = determine_occurrences(processed_list)
        word_to_count = insert_name(word_to_count, "**OCCURRENCE BASED MODEL**")
    elif model_selection == "value":  # Creates a dictionary based on value applied to word
        word_to_count = allocate_values(processed_list)
        word_to_count = insert_name(word_to_count, "**WORD-VALUES BASED MODEL**")
    elif model_selection == "length":  # Creates a dictionary based on length of word
        word_to_count = determine_length(processed_list)
        word_to_count = insert_name(word_to_count, "**WORD-LENGTH BASED MODEL**")
    else:  # Creates a dictionary based on alphabetical sorting
        word_to_count = sort_alphabetically(processed_list)
        word_to_count = insert_name(word_to_count, "**ALPHABETICAL BASED MODEL**")
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


def determine_occurrences(list_data):
    """Add list to dictionary with value based on occurrence."""
    word_to_occurrence = {}
    for word in list_data:
        word_to_occurrence[word] = list_data.count(word)
    return word_to_occurrence


def allocate_values(list_data):
    """Add list to dictionary with value based on nominated keywords."""
    word_to_occurrence = {}
    for word in list_data:
        word_to_occurrence[word] = 1
        if word in WORDS_WITH_VALUE:
            word_to_occurrence[word] = (list_data.count(word) * 5)
    return word_to_occurrence


def determine_length(list_data):
    """Add list to dictionary with value based on length of word."""
    word_to_occurrence = {}
    for word in list_data:
        word_to_occurrence[word] = len(word)
    return word_to_occurrence


def sort_alphabetically(list_data):
    """Add list to dictionary with value based on alphabetical order."""
    word_to_occurrence = {}
    list_data.sort()
    for word in list_data:
        word_to_occurrence[word] = 1
    count = len(word_to_occurrence.values())
    for key in word_to_occurrence:
        word_to_occurrence[key] = count
        count -= 1
    return word_to_occurrence


def insert_name(dictionary, name):
    """Insert name of model into dictionary."""
    maximum_value = (max(dictionary.values()) + 10)
    dictionary[name] = maximum_value
    return dictionary


def sort_by_value(dictionary):
    """Sort dictionary by value in descending order."""
    sorted_dictionary = dict(sorted(dictionary.items(), key=operator.itemgetter(1, 0), reverse=True))
    return sorted_dictionary
