def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count = {}
    for char in text:
        lowercased_char = char.lower()
        char_count[lowercased_char] = char_count.get(lowercased_char, 0) + 1
    return char_count

def sort_on(new_dict):
    return new_dict["num"]

def sorted_list(char_count):
    list_of_dicts = []
    for char, num in char_count.items():
        new_dict = {"char": char, "num": num}
        list_of_dicts.append(new_dict)
    list_of_dicts.sort(key=sort_on, reverse=True)
    return list_of_dicts