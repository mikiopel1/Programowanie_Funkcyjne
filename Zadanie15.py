def custom_sort(lst, key_func):
    return sorted(lst, key=key_func)

# Przykład użycia:
words = ["apple", "banana", "orange", "kiwi"]
sorted_words = custom_sort(words, key=lambda x: len(x))
print("Sorted words by length:", sorted_words)
