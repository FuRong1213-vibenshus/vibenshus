def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + last
    return full_name.title()

## Failing case
"""def get_formatted_name(first, middle, last):
    
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()
"""
## Fixing
"""def get_formatted_name(first, last, middle=''):
    
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
"""