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
