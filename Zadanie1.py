#Zadanie1
from functions import Function

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def is_even(num):
    return num % 2 == 0

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def calculate_average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

def display_results():
    nums = [1, 2, 3, 4, 5]
    print("Addition:", add(4, 6))
    print("Multiplication:", multiply(4, 6))
    print("Is 6 even?", is_even(6))
    print("Is 7 prime?", is_prime(7))
    print("Average:", calculate_average(nums))

if __name__ == "__main__":
    print("#Zadanie1")
    display_results()