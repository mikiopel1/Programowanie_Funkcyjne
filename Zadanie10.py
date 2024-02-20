# Zadanie10

def fibonacci_generator():
    """
    Generator nieskończonego ciągu liczb Fibonacciego.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    print("#Zadanie10 - Fibonacci")
    fib_gen = fibonacci_generator()
    for i in range(10):  # Wyświetl pierwsze 10 liczb Fibonacciego
        print(next(fib_gen))
# Zadanie10 - Czytanie dużej pliku linia po linii

def read_large_file(file_path):
    """
    Generator czytający duży plik tekstowy linia po linii.
    """
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

if __name__ == "__main__":
    print("#Zadanie10 - Czytanie dużej pliku linia po linii")
    file_path = 'duzy_plik.txt'  # Zakładam, że plik o nazwie 'duzy_plik.txt' istnieje w katalogu bieżącym
    lines_gen = read_large_file(file_path)
    for i in range(5):  # Wyświetl pierwsze 5 linii z pliku
        print(next(lines_gen))
