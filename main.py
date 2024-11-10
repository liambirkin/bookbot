path_to_file = "books/frankenstein.txt"

def words_in_text(text):
    words = text.split()
    return len(words) 

def characters_in_text(text):
    text_lowercase = text.lower()
    char_dict = {}
    for char in text_lowercase:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def get_char_dict_list(char_dict):
    char_dict_list = []
    for key, value in char_dict.items():
        if key.isalpha():
            char_dict_list.append({"char": key, "num": value})

    return char_dict_list

def sort_on(dict):
    return dict["num"]


def main():
    with open(path_to_file) as f:
        file_contents = f.read()
        num_words = words_in_text(file_contents)
        char_dict = characters_in_text(file_contents)
        char_dict_list = get_char_dict_list(char_dict)
        char_dict_list.sort(reverse=True, key=sort_on)
        
        print(f"--- Begin report of {path_to_file} ---")
        print(f"{num_words} words found in the document")
        for char in char_dict_list:
            print(f"""The '{char["char"]}' character was found {char["num"]} times""")
        print("--- End report ---")

main()
