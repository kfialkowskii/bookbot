from stats import *
import sys
def get_book_text(filepath):
    """Reads contents of the file
    :param filepath: string - filepath to a file
    :return: string - contents of the file

    This function gets filepath as input
    Reads and saves its contents to a string
    Returns that string
    """
    with open(filepath) as book:
        book_contents = book.read()
    return book_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {count_words_in_book(get_book_text(filepath))} total words")
        print("--------- Character Count -------")
        for dictionary in dict_sort(char_count(get_book_text(filepath))):
            if dictionary["char"].isalpha():
                print(f"{dictionary["char"]}: {dictionary["num"]}")
        print("============= END ===============")

main()
