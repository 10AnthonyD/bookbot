def get_num_words(text):
    text_list  = text.split()
    count = 0
    for i in text_list:
        count += 1
    return count  

def get_char_count(text):
    text_lower_case = text.lower()
    char_dict = {}
    for char in text_lower_case:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["count"]

def sort_dict(dict):
    list_of_dicts = []
    for char in dict:
        count = dict[char]
        new_dict ={"character" : char , "count" : count}
        list_of_dicts.append(new_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

