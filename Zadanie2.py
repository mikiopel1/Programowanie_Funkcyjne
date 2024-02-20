#Zadanie2
from functions import Function


class Main:
    def __init__(self):
        pass

    def display_result(self):
        result = Function.simple_function(3)  # Wywołanie funkcji simple_function z klasy Function
        print("Wynik funkcji:", result)

if __name__ == "__main__":
    print("#Zadanie2")
    main_obj = Main()
    main_obj.display_result()