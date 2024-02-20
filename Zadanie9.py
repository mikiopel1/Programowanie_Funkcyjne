# Zadanie9

from functools import reduce

class Task9:
    @staticmethod
    def find_max(x, y):
        return x if x > y else y

    @staticmethod
    def calculate_average(numbers):
        return reduce(lambda x, y: x + y, numbers) / len(numbers)

    @staticmethod
    def run():
        numbers = [3, 8, 1, 5, 9, 2, 7]

        max_number = reduce(Task9.find_max, numbers)
        print("#Zadanie9")
        print("Największa liczba:", max_number)

        average = Task9.calculate_average(numbers)
        print("Średnia z listy liczb:", average)

if __name__ == "__main__":
    task9 = Task9()
    task9.run()
