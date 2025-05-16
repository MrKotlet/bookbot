from stats import get_num_words
from stats import count_letters
from stats import sort_letters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
        return content

def createReport(nw, sorte):
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print(f"Found {nw} total words")
    print("--------- Character Count -------")

    for l in sorte:
        print(f"{l['l']}: {l['count']}")

    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    # print(f"{get_num_words(text)} words found in the document")
    lib = count_letters(text)
    # print(lib)
    sorte = sort_letters(lib)
    # print(sorte)
    createReport(get_num_words(text), sorte)

main()
