
# ? Q13. Python program to find the roots of a quadratic equation.


import math as m

a, b, c = float(input("Enter the coefficient a: ")), float(input("Enter the coefficient b: ")), float(input("Enter the coefficient c: "))
discriminant = b**2 - 4*a*c

if discriminant > 0:
    print(
        f"Two distinct real roots: {(-b + m.sqrt(discriminant)) / (2*a)} and {(-b - m.sqrt(discriminant)) / (2*a)}")
elif discriminant == 0:
    print(f"One real root: {-b / (2*a)}")
else:
    realPart = -b / (2*a)
    imaginaryPart = m.sqrt(-discriminant) / (2*a)
    print(f"Complex roots: {realPart} + {imaginaryPart}i and {realPart} - {imaginaryPart}i")
