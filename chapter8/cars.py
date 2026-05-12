def infomration_about_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model # Supposed to be a dictionary but I have a list. 
    return car_info #{}
car = infomration_about_car('subaru', 'outback', color='blue', tow_package=True)
print(car) 

# The ** allows us to build car information like color, tow package, and etc.