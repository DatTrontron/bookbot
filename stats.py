def get_file_contents(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(file_contents):
    return len(str.split(file_contents))

def get_characters_nb(file_contents):
    char_count = {}
    for char in str.lower(file_contents):
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count    

book_path = "books/frankenstein.txt"
text = get_file_contents(book_path)
num_words = get_num_words(text)
char_dict = get_characters_nb(text)

def get_list(char_dict):
    char_list = []
    for char in char_dict:
        num = char_dict[char]
        item = {"char": char, "num": num}
        char_list.append(item)
    return char_list

char_list = get_list(char_dict)

def sort_on(item):
    return item["num"]
