def format_cities(name,country,population=''):
    """returns a well formatted city name"""
    if population:
        city_name = f'{name}, {country} - population {population}'
    else:  
        city_name =  f'{name}, {country}'
    return city_name.title()

