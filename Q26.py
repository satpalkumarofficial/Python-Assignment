
# ? 26. Python program to check leap year.


def is_leap_year(year):
    return True if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else False

y = int(input("Enter a year: "))

print(f"{y} is a leap year.") if is_leap_year(y) else print(f"{y} is not a leap year.")
