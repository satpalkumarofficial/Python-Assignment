
# ? Q14. Python program to print the numbers from a given number n till 0 using recursion.

def print_numbers(n):
    if n < 0:
        return
    print(n)
    print_numbers(n - 1)

print_numbers(int(input("Enter a number: ")))
