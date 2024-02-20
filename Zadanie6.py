# Zadanie6

class Task6:
    @staticmethod
    def run():
        # Lista słów
        words = ['apple', 'banana', 'avocado', 'orange', 'grape', 'apricot']

        # Funkcja, która filtruje słowa zaczynające się na literę 'a'
        filtered_words = list(filter(lambda word: word.startswith('a'), words))

        # Lista liczb
        numbers = [1, 2, 3, 4, 5]

        # Funkcja, która oblicza kwadraty liczb
        squared_numbers = list(map(lambda x: x ** 2, numbers))

        print("#Zadanie6")
        print("Słowa zaczynające się na literę 'a':", filtered_words)
        print("Kwadraty liczb:", squared_numbers)

if __name__ == "__main__":
    task6 = Task6()
    task6.run()
