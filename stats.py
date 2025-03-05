def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def get_num_words(filepath):
    text = get_book_text(filepath)
    split = text.split()
    return len(split)

def get_count_characters(text):
    dictionary = {}
    for character in text:
        lowered = character.lower()
        if (lowered in dictionary):
            dictionary[lowered] += 1
        else:
            dictionary[lowered] = 1
    return dictionary

def sorted_count_characters(dictionary):
     tuples = dictionary.items()
     sorted_list = sorted(tuples, reverse=True, key=lambda tuples: tuples[1])
     return sorted_list