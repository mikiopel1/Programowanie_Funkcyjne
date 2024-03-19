def sum_of_squares_of_odds(lst):
    return sum(x**2 for x in lst if x % 2 != 0)

# Przykład użycia:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_of_squares = sum_of_squares_of_odds(numbers)
print("Sum of squares of odds:", sum_of_squares)
