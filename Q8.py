
# ? Q8. Python program to find the sum of the digits of an integer using a while loop.

num = int(input("Enter number to find the sum of the digits of an integer: "))
sod = 0
while num > 0:
    sod += num % 10
    num //= 10

print(f"sum of the digits: {sod}")
