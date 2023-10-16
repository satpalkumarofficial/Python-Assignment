
# ? Q12. Python program to generate the prime numbers from 1 to N.


def is_prime(number):
    return False if number <= 1 else True if number == (2 or 3) else False if number % (2 or 3) == 0 else True

n = int(input("Enter a number: "))
print(f"All prime numbers from 1 to {n}:")
for i in range(n):
    if is_prime(i):
        print(i)
