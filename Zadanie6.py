def map_nested(func, nested_list):
    return [map_nested(func, x) if isinstance(x, list) else func(x) for x in nested_list]

# Przykład użycia:
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mapped_list = map_nested(lambda x: x * 2, nested_list)
print(mapped_list)
