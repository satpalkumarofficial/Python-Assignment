
# ? Q29. Python program to print all the items in a dictionary.

def print_dictionary_items(d):
    print("Dictionary items:")
    for key, value in d.items():
        print(f"{key}: {value}")


my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print_dictionary_items(my_dict)
