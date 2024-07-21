def count_duplicate_characters(s):
    # Create a dictionary to store character frequencies
    char_count = {}

    # Convert the string into a list of characters
    char_list = list(s)

    # Count the frequency of each character
    for char in char_list:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Print characters with a frequency greater than 1
    for char, count in char_count.items():
        if count > 1:
            print(f"{char} : {count}")

# Driver code
if __name__ == "__main__":
    # Given string
    s = "geeksforgeeks"

    # Function call
    count_duplicate_characters(s)