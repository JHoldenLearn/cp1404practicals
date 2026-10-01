"""
asks the user for a password, with error-checking to repeat if the password doesn't meet a minimum length set by a CONSTANT
"""

MINIMUM_LENGTH = 7

password = input("Enter password: ")
while len(password) < MINIMUM_LENGTH:
    print(f"Password must be at least {MINIMUM_LENGTH} characters")
    password = input("Enter password: ")

print("*" * len(password))