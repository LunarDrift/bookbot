import sys


from stats import get_word_count, get_char_count, sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
        return book_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    num_words = get_word_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    character_count = get_char_count(text)
    sorted_chars = sorted_list(character_count)
    for item in sorted_chars:
        char = item["char"]
        count = item["num"]

        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
main()