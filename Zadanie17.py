def capitalize_all_words(string):
    return ' '.join(word.capitalize() for word in string.split())

# Przykład użycia:
sentence = "hello world python"
capitalized_sentence = capitalize_all_words(sentence)
print("Capitalized sentence:", capitalized_sentence)
