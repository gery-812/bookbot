import sys

def get_words(text):
    words = text.split()
    number = len(words)
    return number


def get_book_text(file_path):
    with open(file_path) as f:
        text = f.read()
        
        return text

def character_counter(text):
    lower_text = text.lower()
    char_count = {}
    for char in lower_text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


def sort_characters():
    if len(sys.argv) != 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    characters = character_counter(text)
    alphabet_characters = {char: count for char, count in characters.items() if char.isalpha()}
    sorted_characters = sorted(alphabet_characters.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_characters:
        print(f"{char}: {count}")

   
    


sort_characters()
