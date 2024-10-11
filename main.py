def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    char_count = get_count_characters(text)
    sorted = sort_char_count(char_count)
    for i in sorted:
        print(f"The '{i['character']}' was found {i['occurances']} times")
    print("--- End report ---")

def sort_char_count(char_count: dict):
    def sort_on(dict):
        return dict["occurances"]
    list_of_dicts = []
    for i in char_count:
        if i.isalpha():
            list_of_dicts.append({"character": i, "occurances": char_count[i]})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts


def get_count_characters(text):
    alpha_dict = {}
    for i in text.lower():
        if i not in alpha_dict:
            alpha_dict[i] = 1
        else:
            alpha_dict.update({i: alpha_dict[i] + 1})
    return alpha_dict

# def get_chars_dict(text):
#     chars = {}
#     for c in text:
#         lowered = c.lower()
#         if lowered in chars:
#             chars[lowered] += 1
#         else:
#             chars[lowered] = 1
#     return chars

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
