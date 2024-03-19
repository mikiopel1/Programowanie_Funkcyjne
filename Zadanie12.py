def rotate_list(lst, steps):
    if not lst:
        return lst
    steps = steps % len(lst)
    return lst[-steps:] + lst[:-steps]

# Przykład użycia:
my_list = [1, 2, 3, 4, 5]
rotated = rotate_list(my_list, 2)
print("Rotated list:", rotated)
