
# ? Q25. Python program to implement matrix multiplication.


# 3x3 matrix
x = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

# 3x4 matrix
y = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]


# result is 3x4
for r in [[sum(a*b for a, b in zip(x_r, y_c)) for y_c in zip(*y)] for x_r in x]:
    print(r)
