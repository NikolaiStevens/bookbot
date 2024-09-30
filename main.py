def count_characters(text):
    # Convert the text to lowercase
    text = text.lower()

    # Create an empty dictionary to store character counts
    char_count = {}

    # Loop through each character in the text
    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count

def main():
    # Open the file and read the contents
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    # Count the number of words
    word_count = len(file_contents.split())
    
    # Count the characters in the text
    char_count = count_characters(file_contents)

    # Print the report
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    # Sort characters by their count in descending order and print
    sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

main()
