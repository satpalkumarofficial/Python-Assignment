
# ? Q28. Python program to print Fibonacci series using iteration. 

def fibonacci_iterative(n):
    fibonacci_series = []

    a, b = 0, 1
    for _ in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b

    return fibonacci_series

n = int(input("Enter the number of terms in the Fibonacci series: "))

print("The number of terms should be a positive integer." if n <= 0 else f"Fibonacci series:\n{fibonacci_iterative(n)}")

