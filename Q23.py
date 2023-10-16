
# ? Q23. Python program to check whether a string is palindrome or not. 

def is_palindrome(s):
    
    s = s.replace(" ", "").lower()
    
    return s == s[::-1]


string = input("Enter a string: ")

print(f"'{string}' is a palindrome." if is_palindrome(string) else f"'{string}' is not a palindrome.")
