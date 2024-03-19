def safe_function(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    return wrapper

@safe_function
def divide(a, b):
    return a / b

print(divide(10, 0))
