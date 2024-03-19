def find_max_min_diff(lst):
    if not lst:
        return None
    return max(lst) - min(lst)

# Przykład użycia:
numbers = [10, 7, 23, 4, 18]
diff = find_max_min_diff(numbers)
print("Difference between max and min:", diff)
