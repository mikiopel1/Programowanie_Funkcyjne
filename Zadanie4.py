# Zadanie4

def apply_function(func, x, y):
    """
    Funkcja przyjmuje inną funkcję jako argument oraz dwa argumenty x i y,
    a następnie wykonuje tę funkcję dla podanych argumentów x i y.
    """
    return func(x, y)

def add(x, y):
    """Funkcja dodaje dwa argumenty x i y."""
    return x + y

def subtract(x, y):
    """Funkcja odejmuje drugi argument y od pierwszego argumentu x."""
    return x - y

def multiply(x, y):
    """Funkcja mnoży dwa argumenty x i y."""
    return x * y

if __name__ == "__main__":
    print("#Zadanie4")
    # Przykładowe użycie funkcji apply_function z różnymi funkcjami jako argumentem
    print("Dodawanie:", apply_function(add, 5, 3))
    print("Odejmowanie:", apply_function(subtract, 10, 4))
    print("Mnożenie:", apply_function(multiply, 2, 6))