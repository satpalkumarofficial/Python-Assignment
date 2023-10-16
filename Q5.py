
# ? Q5. Python program to check whether the given integer is a multiple of both 5 and 7.


num = int(input("Enter an integer: "))

print("Your input is multiple of 5 and 7." if num % 7 == 0 and num %
      5 == 0 else "Your input is not a multiple of 5 and 7")
