def main():
    book_path = "books/frankenstein.txt"
    print_book_report(book_path)


def count_strings(text_string):
    words = text_string.split()
    return len(words)

def count_letters(text_string):
    lowered_string = text_string.lower()
    letter_dict = {}
    for letter in lowered_string:
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def print_book_report(path):
    book_text = get_book_text(path)
    word_count = count_strings(book_text)
    letter_dict = count_letters(book_text)
    letter_list = turn_dict_into_list(letter_dict)
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    for letter_tuple in letter_list:
        print(f"The {letter_tuple[0]} character was found {letter_tuple[1]} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def turn_dict_into_list(dict):
    letter_list = list(dict.items())
    letter_list.sort(key=lambda a: a[1], reverse=True)
    return letter_list

if __name__ == "__main__":
    main()