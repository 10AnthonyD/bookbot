from stats import get_num_words
from stats import get_char_count
from stats import sort_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
file_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        read_file = f.read()
    return read_file
    
def main():
    count = get_num_words(get_book_text(file_path))
    
    char_dict = get_char_count(get_book_text(file_path))
    list_of_dicts = sort_dict(char_dict)

    print("=" * 12, "BOOKBOT", "=" * 12)
    print(f"Analyzing book found at {file_path}...")
    print("-" * 11, "Word Count", "-" * 10)
    print(f"Found {count} total words")
    print("-" * 9, "Character Count", "-" * 7)

    for dict in list_of_dicts:
        char = dict["character"]
        count = dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("=" * 13, "END", "=" * 15)

main()