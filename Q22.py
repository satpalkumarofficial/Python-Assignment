
# ? Q22. Python program to delete an element from a list by index.

def delete_element_by_index(list, index):
    if index < 0 or index >= len(list):
        print("Invalid index. Deletion failed.")
    else:
        del list[index]
        print(f"Element at index {index} deleted.")
    return list

numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)

delete_index = int(input("Enter the index to delete: "))

new_numbers = delete_element_by_index(numbers, delete_index)
print("Updated list:", new_numbers)


# ! by pop method
# def delete_element_by_index(list, index):
#     if index < 0 or index >= len(list):
#         print("Invalid index. Deletion failed.")
#     else:
#         element = list.pop(index)
#         print(f"Element at index {index} ({element}) deleted.")
#     return list

# numbers = [1, 2, 3, 4, 5]
# print("Original list:", numbers)

# delete_index = int(input("Enter the index to delete: "))

# new_numbers = delete_element_by_index(numbers, delete_index)
# print("Updated list:", new_numbers)
