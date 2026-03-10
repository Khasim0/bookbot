
def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def get_num_words(string):
    words = string.split()
    num_words = 0   
    for word in words:
        num_words += 1
    
    return num_words 

def main():
    result = get_book_text("books/frankenstein.txt")
    
    num_words = get_num_words(result)
    print (f"(Found {num_words} total words)")  
main()


