def get_num_words (text):
  return len(text.split())

def get_chars_dict (text):
  alpha_dic = {}

  for alpha in text.lower():
    if alpha in alpha_dic:
      alpha_dic[alpha] += 1
    else:
      alpha_dic[alpha] = 1

  return alpha_dic

def chars_dict_to_sorted_list (dic):
  return sorted(dic.items(), key=lambda x: x[1], reverse=True)