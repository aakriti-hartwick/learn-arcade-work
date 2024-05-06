import re

# This function takes in a line of text and returns
# a list of words in the line.


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    my_file = open("dictionary.txt")

    # Create an empty list to store our names
    dictionary_list = []

    # Loop through each line in the file like a list
    for line in my_file:
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()

        # Add the name to the list
        dictionary_list.append(line)
    my_file.close()
    print("There were", len(dictionary_list), "names in the file.")

    # --- Linear search
    print("---Linear search---")

#    key = "ABJURE"
#    found = False
    my_file = open("AliceInWonderland200.txt")
    # Create an empty list to store our names
    # Loop through each line in the file like a list
    for index, line in enumerate(my_file):
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()
        wordlist = split_line(line)

        for word in wordlist:
            linear_search(dictionary_list, word.upper(), index+1)
    my_file.close()

    print('---Binary Search---')
    my_file = open("AliceInWonderland200.txt")
    # --- Binary search
    for index, line in enumerate(my_file):
        # Remove any line feed, carriage returns or spaces at the end of the line

        line = line.strip()
        wordlist = split_line(line)

        for word in wordlist:
            binary_search(dictionary_list, word.upper(), index+1)


def linear_search(name_list, key, index):
    # --- Linear search
    # Start at the beginning of the list
    current_list_position = 0

    # Loop until you reach the end of the list, or the value at the
    # current position is equal to the key
    while current_list_position < len(name_list) and name_list[current_list_position] != key:
        # Advance to the next item in the list
        current_list_position += 1

    if current_list_position < len(name_list):
        return True
    else:
        print(f"Line {index}  not found: {key}")


def binary_search(list, key, index):
    lower_bound = 0
    upper_bound = len(list) - 1
    found = False
    while lower_bound <= upper_bound and not found:

        # Find the middle position
        middle_pos = (lower_bound + upper_bound) // 2

        # Figure out if we:
        # move up the lower bound, or
        # move down the upper bound, or
        # we found what we are looking for
        if list[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif list[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True

    if found:
        return True
    else:
        print(f"Line {index} not found:{key}")

main()
