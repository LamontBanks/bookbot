# Load and print file to console
# https://docs.python.org/3.12/tutorial/inputoutput.html#tut-files
def main():
    file_path = 'books/frankenstein.txt'
    file_contents = read_text_from_file('books/frankenstein.txt')

    print(f"Contents of {file_path}")
    print(file_contents)

    # Word count
    num_words = word_count(file_contents)
    print(f"There are {num_words} words in {file_path}")

    # Unique Character count
    char_count_dict = count_unique_char(file_contents)
    print(f"Unique characters: {char_count_dict}")

    # Sort unique characters by count, descending:
    # Create a list of tuples from the dictionary, then sort by the character count (index=1)
    char_count_freq_tuples = []
    for char in char_count_dict:
        char_count_freq_tuples.append((char, char_count_dict[char]))

    # https://docs.python.org/3.12/howto/sorting.html#key-functions
    char_count_freq_tuples_sorted = sorted(char_count_freq_tuples, key=lambda char_count: char_count[1], reverse=True)
    for char_count_tuple in char_count_freq_tuples_sorted:
        print(f"The '{char_count_tuple[0]}' character was found {char_count_tuple[1]} times")


# Helper functions

def read_text_from_file(relative_path_to_file):
    text = ""

    if (relative_path_to_file != None):
        with open(relative_path_to_file, encoding="utf-8") as f:
            text = f.read()
    
    return text

def word_count(str):
    if (str != None):
        return len(str.split())
    else:
        return 0

# Not case-sensitive
# Ignore nor alphabet chars
def count_unique_char(str):
    unique_char_dict = {}

    # Convert to lower case for case-insensitivity
    lower_case_str = str.lower()

    for char in lower_case_str:
        if (char.isalpha()):
            if (char not in unique_char_dict):
                unique_char_dict[char] = 1
            else:
                unique_char_dict[char] += 1
    
    return unique_char_dict

main()

