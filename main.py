# Load and print file to console
# https://docs.python.org/3.12/tutorial/inputoutput.html#tut-files
def main():
    file_path = 'books/frankenstein.txt'
    file_contents = read_text_from_file('books/frankenstein.txt')

    print(f"Contents of {file_path}")
    print(file_contents)
    print(f"There are {word_count(file_contents)} words in {file_path}")

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

main()

