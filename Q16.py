
# ? Q16. Python program to display the sum of n numbers using a list. 


n = int(input("Enter the number of elements: "))

nums = []

for i in range(n):
    nums.append(float(input(f"Enter number {i + 1}: ")))

print(f"The sum of {n} numbers is: {int(sum(nums))}")
