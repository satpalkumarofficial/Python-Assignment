
# ? Q17. Python program to implement linear search. 

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target element
    return -1  # Return -1 if the target element is not found


arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target = 5
result = linear_search(arr, target)

print(f"Element {target} found at index {result}." if result != -1 else f"Element {target} not found in the list.")