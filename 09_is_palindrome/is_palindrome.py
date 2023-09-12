def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    string = phrase[::-1].replace(" ","")
    if string.lower() == phrase.lower().replace(" ",""):
        print(f"{string.lower()} | {phrase.lower()}")
        return True
    else: 
        print(f"{string.lower()} | {phrase.lower()}")
        return False