import sys
from stats import *

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print_structured(book_path)
    

def print_structured(filepath):
    num_count = get_num_words(filepath)
    character_count = get_count_characters(get_book_text(filepath))
    sorted_characters = sorted_count_characters(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_count} total words")
    print("--------- Character Count -------")
    print_list(sorted_characters)
    print("============= END ===============")

def print_list(list):
    for item in list:
        if (item[0].isalpha()):
            print(f"{item[0]}: {item[1]}")

main()