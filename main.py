def count_characters(text):
    character_count = {}
    lowered_text = text.lower()
    for character in lowered_text:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def count_words(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open(path) as f:
        return f.read()

def sort_on(char_dict):
    return char_dict["count"]

def get_sorted_counts(unsorted_counts):
    char_counts_list = []
    for character in unsorted_counts:
        char_dict = {
            "character": character, 
            "count" : unsorted_counts[character]
        }
        char_counts_list.append(char_dict)
    char_counts_list.sort(reverse=True, key=sort_on)
    return char_counts_list

def report(path):
    print(f"--- Begin report of {path} ---")

    text = get_text(path)
    count = count_words(text)

    print(f"{count} words found in the document")
    print()

    sorted_char_counts = get_sorted_counts(count_characters(text))
    for char_dict in sorted_char_counts:
        character = char_dict["character"]
        char_count  = char_dict["count"]
        if character.isalpha():
            print(f"The {character} was found {char_count} times")
            
    print("-- End report --")

def main():
    report("books/frankenstein.txt")


main()