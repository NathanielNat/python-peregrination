def cities(city,country,population=''):
    if population:
        location = f'{city}, {country} - population {population}'
    else:
        location = f'{city}, {country}'
    return location.title()

    