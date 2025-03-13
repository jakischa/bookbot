from stats import word_counter
from stats import letter_counter, sorted_list
import sys

if len(sys.argv) != 2:
    print ("Usage: python3 main.py <path_to_book>") 
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



def main():
    filepath = sys.argv[1]
    book_text = get_book_text(sys.argv[1])
    print(f"Analyzing book at: {filepath}")
    word_count =word_counter(book_text)
  #  print (f"{word_count} words found in the document")

    letter_counts = letter_counter(book_text)
  #  print(letter_counts)
    sort = sorted_list(letter_counts)
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {sys.argv[1]}...")
    print ("----------- Word Count ----------")
    print (f"Found {word_count} total words")
    print ("--------- Character Count -------")
    for i in sort:
        if i["character"].isalpha():
            print(f"{i['character']}: {i['count']}")




main()

