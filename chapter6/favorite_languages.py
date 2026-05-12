favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
friends = ['phil','sarah']
print(favorite_languages)
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
for name, language in favorite_languages.items():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()},I see you love {language}")
    print(f"{name.title()}'s favorite language is {language.title()}.")
    for name in sorted(favorite_languages.keys()):
        print(f"{name.title()}, Thank you for taking the poll.")
print("The following languages have been mentioned:")
