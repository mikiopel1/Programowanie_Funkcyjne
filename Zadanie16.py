def remove_whitespace(lst):
    return [word.replace(" ", "") for word in lst]

# Przykład użycia:
strings = ["  Hello ", "World  ", " Python "]
cleaned_strings = remove_whitespace(strings)
print("Strings without whitespace:", cleaned_strings)
