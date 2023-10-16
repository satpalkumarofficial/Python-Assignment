
# ? Q7. Python program to find the geometric mean of n numbers. 

import math as m

n = int(input("Enter the number of values: "))
values = []

for i in range(n):
    value = float(input(f"Enter value {i + 1}: "))
    values.append(value)


product = 1
for value in values:
    product *= value # Product of all values

geo_mean = m.pow(product, 1/n)

print(f"Geometric Mean: {geo_mean}")
