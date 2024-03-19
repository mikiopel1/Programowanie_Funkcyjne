def zip_with_index(lst):
    return [(index, value) for index, value in enumerate(lst)]

# Przykład użycia:
words = ["apple", "banana", "orange", "kiwi"]
indexed_words = zip_with_index(words)
print(indexed_words)
