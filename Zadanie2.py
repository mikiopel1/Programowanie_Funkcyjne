from itertools import combinations

def get_combinations(elements):
    return list(combinations(elements, 2))

elements = [1, 2, 3, 4]
print(get_combinations(elements))
