
# ? Q21. Python program to insert a number to any position in a list. 

def insert_number_at_position(list, num, position):
    if position < 0:
        print("Position cannot be negative.")
    elif position > len(list):
        print("Position exceeds the list length.")
    else:
        list.insert(position, num)
        print(f"{num} inserted at position {position}.")
    return list

numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)

num_to_insert = int(input("Enter a number to insert: "))
insert_position = int(input("Enter the position to insert: "))

new_numbers = insert_number_at_position(numbers, num_to_insert, insert_position)
print("Updated list:", new_numbers)
