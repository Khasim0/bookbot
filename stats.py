from main import get_book_text
def get_num_words(string):
    words = string.spilt()
    num_words = 0
    for word in words:
        num_words += word
    return words 
print (f"(Found {num_words} total words)")

# in -  new funtion get text  from book as string. import from main
# out - return number of time each character(symbol and space as well), return dict of string: integer
# rule - 

def get_num_words(filepath):
    char= filepath.lower()
    num_char = {}
    for c in char:
        num_char = num_words
print num_char