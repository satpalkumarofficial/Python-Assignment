
# ? Q6. Python program to display the given integer in a reverse manner.

num = int(input("Enter integer: "))
rev_num = 0

while num > 0:
    rev_num = rev_num * 10 + num % 10
    num //= 10
print(f"Reversed integer: {rev_num}")

# print(f"Reversed integer: {str(int(input('Enter integer: ')))[::-1]}") # By python's inbuilt str() function
