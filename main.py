def get_text(path):
    with open(path) as f:
        return f.read()

def main():
    text = get_text("books/frankenstein.txt")
    print(text)

main()