def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    Day = {
        1 : 'Sunday',
        2 : 'Moday',
        3 : 'Tuesday',
        4 : 'Wednesday',
        5 : 'Thursday',
        6 : 'Friday',
        7 : 'Saturday'
    }
    name = Day.get(day_of_week)
    if name:
        return name
    else:
        return "None"