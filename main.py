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

def main():
    text = get_text("books/frankenstein.txt")
    count = count_words(text)
    print(f"{count} words found in the text")
    char_counts = count_characters(text)
    print(char_counts)

main()