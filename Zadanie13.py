def split_list(lst, chunk_size):
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

# Przykład użycia:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunks = split_list(numbers, 3)
print("Split list:", chunks)
