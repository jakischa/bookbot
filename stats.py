

def word_counter(book_text):
    
    word_count = 0
    words = book_text.split()
    for word in words:
        word_count += 1
    return word_count

def letter_counter(book_text):
    char_counts = {}
    for character in book_text:

        character = character.lower()
        if character in char_counts:
            char_counts[character] += 1
        else:
            char_counts[character] = 1
    return char_counts
        
def sorted_list(dictionary):
    character_counts = [{"character": char, "count":count}
                        for char, count in dictionary.items()]
    

    character_counts.sort(reverse=True, key=lambda item: item["count"])
    return character_counts
