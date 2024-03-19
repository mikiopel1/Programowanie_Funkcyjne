from itertools import groupby

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

groups = {k: list(g) for k, g in groupby(numbers, key=lambda x: x % 2 == 0)}
print(groups)
