
def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    character_dict={}
    for char in text:
        if char.lower() in character_dict:
            character_dict[char.lower()] += 1
        else:
            character_dict[char.lower()] = 1
    return character_dict



def sorted_characters(character_dict:dict):
    sorted_list=[]
    def sort_on(items):
        return items["num"]

    for key, value in character_dict.items():
        if key.isalpha():
            sorted_list.append({"char": key, "num": value})

    sorted_list.sort(reverse=True,key=sort_on )
    return sorted_list