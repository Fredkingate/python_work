def city_country():
    """Retrn a string of the form City, Country."""""
    city = input("Please enter the name of a city: ")
    country = input("Please enter the name of a country: ")
    city_country = f"{city}, {country}"
    print(city_country.title())
    return city_country
city_country()