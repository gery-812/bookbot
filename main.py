from stats import get_words

from stats import get_book_text

from stats import character_counter

from stats import sort_characters

import sys

def main():
    if len(sys.argv) != 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)
    words = get_words(text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    sort_characters()
    print("============= END ===============")
    return     


main()

