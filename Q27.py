
# ? Q27. Python program to find the Nth term in a Fibonacci series using recursion. 

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = int(input("Enter the value of N: "))

print("N should be a non-negative integer." if n < 0 else f"The {n}-th term in the Fibonacci series is: {fibonacci_recursive(n)}")
