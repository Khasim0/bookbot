def get_num_words(string):
    words = string.split()
    num_words = 0   
    for word in words:
        num_words += 1
    
    return num_words 

def get_num_char(filepath):
    char= filepath.lower()
    num_char = {}
    for c in char:
        if c in num_char:
            num_char[c] += 1
        else:
            num_char[c] = 1
        
    return num_char

def sort_on(items):
        return items ['num']

def get_char_counts( num_words, num_char ):
    sorted_list =[]

    for key, value in num_char.items():
        sorted_list.append({"char": key, "num": value}) 
    sorted_list.sort(reverse=True, key = sort_on)

    return sorted_list
    
        
