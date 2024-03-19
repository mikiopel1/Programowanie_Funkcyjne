def filter_long_words(words):
    avg_length = sum(len(word) for word in words) / len(words)
    return [word for word in words if len(word) > avg_length]

# Przykład użycia:
word_list = ["apple", "banana", "orange", "kiwi", "strawberry"]
filtered_words = filter_long_words(word_list)
print(filtered_words)
