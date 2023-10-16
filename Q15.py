
# ? Q15. Python program to find the factorial of a number using recursion.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter an integer: "))

print("Factorial is not defined for negative numbers." if num < 0 else f"The factorial of {num} is {factorial(num)}")

