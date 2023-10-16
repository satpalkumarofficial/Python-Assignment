

# ? Q20. Python program to find the largest number in a list without using built-in functions.

def find_largest_number(arr):
    if not arr:
        return None

    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest


largest_number = find_largest_number([10, 5, 8, 17, 3, 20, 12, 15])

print(f"Largest number in the list is: {largest_number}") if largest_number is not None else print("List is empty.")
