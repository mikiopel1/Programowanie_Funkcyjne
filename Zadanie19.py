def check_anagrams(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

# Przykład użycia:
word1 = "listen"
word2 = "silent"
are_anagrams = check_anagrams(word1, word2)
print(f"Are '{word1}' and '{word2}' anagrams:", are_anagrams)
