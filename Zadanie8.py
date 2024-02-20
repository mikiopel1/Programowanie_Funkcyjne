# Zadanie8

# Lista zawierająca pierwsze 10 liczb kwadratowych
squared_numbers = [x ** 2 for x in range(1, 11)]

# Lista długości słów
words = ['apple', 'banana', 'avocado', 'orange', 'grape', 'apricot']
words_lengths = [len(word) for word in words]

if __name__ == "__main__":
    print("#Zadanie8")

    # Wyświetlenie listy zawierającej pierwsze 10 liczb kwadratowych
    print("Pierwsze 10 liczb kwadratowych:", squared_numbers)

    # Wyświetlenie listy długości słów
    print("Długości słów:", words_lengths)
