def is_palindrome(input_string):
    # Two variables are initialized as string date types using empty 
    # quotes: "reverse_string" to hold the "input_string" in reverse
    # order and "new_string" to hold the "input_string" minus the 
    # spaces between words, if any are found.
    new_string = ""
    reverse_string = ""

    # Complete the for loop to iterate through each letter of the
    # "input_string"
    for letter in input_string:
        if letter != " ":
            new_string += letter
            reverse_string = letter + reverse_string

    # Check if the cleaned string is equal to its reverse
    return new_string == reverse_string


print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True