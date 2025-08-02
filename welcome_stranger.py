def greetings(name_list, title_dictionary):
    return (f'Hello, {" ".join(name_list)}! Nice to have '
            f'a {title_dictionary["title"]} {title_dictionary["occupation"]} '
            'around.')
greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.