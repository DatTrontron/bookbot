from stats import get_num_words, get_characters_nb, get_file_contents, get_list, sort_on
import sys

def main():

    if len(sys.argv) != 2:
        sys.exit("Usage: python3 main.py <path_to_book>")
    else:
        book_path = sys.argv[1]
        text = get_file_contents(book_path)
        num_words = get_num_words(text)
        char_dict = get_characters_nb(text)
        char_list = get_list(char_dict)
        char_list.sort(reverse=True, key=sort_on)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        for item in char_list:
            ch = item["char"]
            if ch.isalpha():
                print(f"{ch}: {item['num']}")

        print("============= END ===============")

main()