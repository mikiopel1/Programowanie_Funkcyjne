def recursive_sum(numbers):
    total = 0
    for num in numbers:
        if isinstance(num, list):
            total += recursive_sum(num)
        else:
            total += num
    return total

# Przykład użycia:
nested_numbers = [1, [2, 3], [4, [5, 6]]]
print(recursive_sum(nested_numbers))
