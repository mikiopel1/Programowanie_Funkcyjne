# Zadanie5

class Task5:
    @staticmethod
    def filter_even_numbers(numbers):
        """
        Funkcja przyjmuje listę liczb i zwraca listę zawierającą tylko liczby parzyste.
        """
        return list(filter(lambda x: x % 2 == 0, numbers))

    @staticmethod
    def calculate_rectangle_area(length, width):
        """
        Funkcja oblicza pole prostokąta na podstawie długości jego boków.
        """
        return length * width

if __name__ == "__main__":
    print("#Zadanie5")
    task5 = Task5()

    # Przykładowe użycie funkcji filter_even_numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = task5.filter_even_numbers(numbers)
    print("Lista liczb parzystych:", even_numbers)

    # Przykładowe użycie funkcji calculate_rectangle_area
    length = 5
    width = 10
    area = task5.calculate_rectangle_area(length, width)
    print("Pole prostokąta o długościach boków {} i {}: {}".format(length, width, area))
