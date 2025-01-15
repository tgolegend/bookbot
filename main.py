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

main()