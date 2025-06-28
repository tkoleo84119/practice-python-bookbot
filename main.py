from stats import count_words, count_alpha

def get_book_text (path):
  with open(path, 'r', encoding='utf-8') as f:
    return f.read()

def main ():
  book = get_book_text('./books/frankenstein.txt')
  num_words = count_words(book)
  alpha_dic = count_alpha(book)
  print(f"{num_words} words found in the document")
  print(alpha_dic)

main()