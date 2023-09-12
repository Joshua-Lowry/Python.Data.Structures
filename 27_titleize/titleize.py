def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    words = phrase.split()
    title_words = [word.capitalize() for word in words]
    titleized_phrase = ' '.join(title_words)
    return titleized_phrase