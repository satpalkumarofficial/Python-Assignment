
# ? 11. Python program to check whether the given integer is a prime number or not.

def is_prime(number):
    return False if number <= 1 else True if number == (2 or 3) else False if number % (2 or 3) == 0 else True

num = int(input("Enter an integer to check prime or not: "))
print("Your input is a prime number." if is_prime(num) else "Your input is not a prime number.")
