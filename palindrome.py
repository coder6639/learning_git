def is_palindrome(word:str) -> bool:
    """
    Checks if a word is a palindrome, returns True if it is and False if it is not
    Arguments:
    word: word to be checked
    """
    palindrome_string = ""
    for char in word:
        if char.isalnum():
            palindrome_string += char
    return palindrome_string.casefold() == palindrome_string[::-1].casefold()


print(is_palindrome("KobyŁA ma mały bok"))
print(is_palindrome("321 oko 1 2 3"))