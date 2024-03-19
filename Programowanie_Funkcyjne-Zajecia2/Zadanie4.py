numbers = [5, 10, 15, 20]

squares_gt_10 = [x ** 2 for x in numbers if (s := x ** 2) > 10]
print(squares_gt_10)
