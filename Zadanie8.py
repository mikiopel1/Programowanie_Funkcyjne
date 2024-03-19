def partition_list(lst, condition):
    return [x for x in lst if condition(x)], [x for x in lst if not condition(x)]

# Przykład użycia:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even, odd = partition_list(numbers, lambda x: x % 2 == 0)
print("Even:", even)
print("Odd:", odd)
