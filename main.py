from stats import get_num_words, get_num_char, get_char_counts
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents



def main():
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    result = get_book_text(sys.argv[1])
    
    num_words = get_num_words(result)
    num_char = get_num_char(result)
    char_count = get_char_counts(num_words, num_char)
    print (f"Found {num_words} total words")  
    
    for item in char_count:
        print(f"{item['char']}: {item['num']}")


main()

