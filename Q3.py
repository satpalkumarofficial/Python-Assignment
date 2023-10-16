
# ? Q3. Python program to find the product of a set of real numbers.

# A × B = {(a, b) : a ∈ A and b ∈ B}

n = int(input("Enter the number of values: "))
values = []

for i in range(n):
    values.append(float(input(f"Enter value {i + 1}: ")))


product = 1
for value in values:
    product *= value  # Calculate product of all values

print(f"Product of the values: {product}")
