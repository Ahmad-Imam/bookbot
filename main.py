from stats import count_characters, count_words,sorted_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text=get_book_text(sys.argv[1])
    num_words=count_words(book_text)
    char_count=count_characters(book_text)
    sorted_chars=sorted_characters(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("------- Character Count --------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()