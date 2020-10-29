def is_palindrome(word:str) -> bool:
    """
    Checks if a word is a palindrome, returns True if it is and False if it is not
    Arguments:
    word: word to be checked
    """
    palindrome = (word == word[::-1])
    print(palindrome)
    return palindrome

is_palindrome("oko")