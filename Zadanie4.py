def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Przykład użycia:
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(original_list)
print(unique_list)
