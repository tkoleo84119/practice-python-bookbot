from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list

def main ():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  chars_dict = get_chars_dict(text)
  chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
  print_report(book_path, num_words, chars_sorted_list)

def get_book_text (path):
  with open(path, 'r', encoding='utf-8') as f:
    return f.read()

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")
    print("============= END ===============")

main()