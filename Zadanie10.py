def cumulative_sum(lst):
    cumulative = []
    total = 0
    for num in lst:
        total += num
        cumulative.append(total)
    return cumulative

# Przykład użycia:
numbers = [1, 2, 3, 4, 5]
cumulative_sums = cumulative_sum(numbers)
print(cumulative_sums)
