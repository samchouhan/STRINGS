def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""

    for letter in input_string:
        if letter != " ":
            new_string += letter.lower()
            reverse_string = letter.lower() + reverse_string

    if new_string == reverse_string:
        return True
    else:
        return False


print(is_palindrome("Never Odd or Even"))  # True
print(is_palindrome("abc"))                # False
print(is_palindrome("kayak"))              # True