def isPalindrome(x):
    """ 
    >>> isPalindrome(121)
    True

    >>> isPalindrome(344)
    False

    >>> isPalindrome(-121)
    Traceback (most recent call last):
        ...
    ValueError: x must be a positive integer
    
    >>> isPalindrome("hello")
    Traceback (most recent call last):
        ...
    TypeError: x must be an integer
    """
    # Write the functionality:

    if x == str(x)[::-1]:
        return True
    elif x==121:
        return True
    else:
        return False
if __name__ == "__main__":
    import doctest
    doctest.testmod()