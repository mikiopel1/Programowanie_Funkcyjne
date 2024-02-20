#Zadanie7


# Funkcja podnosząca liczbę do kwadratu
def square(x):
    return x ** 2


# Funkcja dodająca 5 do liczby
def add_five(x):
    return x + 5


# Funkcja aplikująca listę funkcji do danej wartości
def apply_functions(values, functions):
    """
    Funkcja aplikuje listę funkcji do danej wartości w kolejności podanej w liście.
    """
    result = values
    for func in functions:
        result = func(result)
    return result


if __name__ == "__main__":
    print("#Zadanie7")
    # Lista funkcji
    functions = [square, add_five]

    # Lista wartości
    values = [1, 2, 3, 4, 5]

    # Aplikacja funkcji do wartości
    results = [apply_functions(value, functions) for value in values]
    print("Wyniki:", results)
