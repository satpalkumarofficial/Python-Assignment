
# ? Q19. Python program to find the odd numbers in an array.

def odd_finder(arr):
    odd_nums = []
    for num in arr:
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums

print(f"Odd numbers in the array: {odd_finder([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}")
