def make_city(city, country, population=''):
    if population:
        cityString = f"{city}, {country}, {population}"
    else:
        cityString =f"{city}, {country}"
    return cityString
