from itertools import product

letters = ['A', 'B']
numbers = ['C', 'D']

combinations = list(product(letters, numbers))
print(combinations)
