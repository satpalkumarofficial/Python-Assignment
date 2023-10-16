
# ? 10. Python program to display all integers within the range 100-200 whose sum of digits is an even number.

dig = 0
for i in range(100, 201):
    n = i
    while n > 0:
        dig += n % 10
        n //= 10
    if dig % 2 == 0:
        print(i)
    dig = 0
