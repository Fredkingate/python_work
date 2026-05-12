# make a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that is being ordered. Call the function three times, using a different number of arguments each time.
def make_sandwich(*toppings):
    """Print a summary of the sandwich that is being ordered."""
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
print(make_sandwich('lettuce', 'tomato', 'bacon'))
print(make_sandwich('turkey', 'avocado'))
print(make_sandwich('ham', 'cheese', 'mustard', 'pickles'))