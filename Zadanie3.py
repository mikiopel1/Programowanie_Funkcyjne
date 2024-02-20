#Zadanie3
global_variable = 10  # Zmienna globalna

def function_with_global_and_local_variables(local_variable):
    # Używamy słowa kluczowego 'global', aby poinformować Pythona, że mamy na myśli zmienną globalną
    global global_variable
    print("Wartość zmiennej globalnej:", global_variable)
    print("Wartość zmiennej lokalnej:", local_variable)

    # Modyfikacja zmiennej globalnej
    global_variable = 20
    print("Nowa wartość zmiennej globalnej:", global_variable)

if __name__ == "__main__":
    print("#Zadanie3")
    function_with_global_and_local_variables(5)
