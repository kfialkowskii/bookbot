def count_words_in_book(book):
    """Counts words in a string
    :param book: string - text as individual string
    :return: int - number of words in a string

    This function takes string as an input
    Counts words in this string
    Returns number of countend words
    """
    word_count = 0
    words = book.split()
    for word in words:
        word_count += 1
    return word_count

def char_count(text):
    """Makes dictionary of characters in text
    :param text: string - text as individual string
    :return: dictionary - character : int of occurences

    This function takes string as input
    Iterates over each character
    Checks if character exist as key in new dictionary
    If it exist it appends value by 1
    If it does not exist it makes char a key and sets its value to 1
    Returns dictionary of all characters with number of occurences
    """
    char_dict = {}
    for char in text:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    return char_dict

def sort_on(items):
    """Helper function for dict_sort
    :param items: dict - takes dictionary
    :return: value of num key in dictionary

    It takes dictionary as an input
    Returns values under "num" key
    """
    return items["num"]

def dict_sort(dictionary):
    """Making list of dictionaries from single dictionary
    :param dictionary: dict - dictionary
    :return: list - reverse-sorted list of two key-values dictionaries

    It takes a dictionary
    Makes new dictionary containing two key-value pairs
    Previous keys and values now are both values
    Setting same keys in each new dictionary
    """
    new_list = []

    for key, value in dictionary.items():
        new_dictionary = {}
        new_dictionary["char"] = key
        new_dictionary["num"] = value
        new_list.append(new_dictionary)

    new_list.sort(reverse=True, key=sort_on)
    
    return new_list
