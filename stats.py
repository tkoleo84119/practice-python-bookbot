def count_words (text):
  return len(text.split())

def count_alpha (text):
  alpha_dic = {}

  for alpha in text.lower():
    if alpha in alpha_dic:
      alpha_dic[alpha] += 1
    else:
      alpha_dic[alpha] = 1

  return alpha_dic