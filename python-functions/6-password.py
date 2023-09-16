#!/usr/bin/python3
#6-password.py

def validate_password(password):
    if len(password) < 8:
        return False

    has_lowercase = False
    has_uppercase = False
    has_digit = False

    # Check each character in the password
    for char in password:
        # Check for uppercase letter
        if char.isupper():
            has_uppercase = True
        # Check for lowercase letter
        elif char.islower():
            has_lowercase = True
        # Check for digit
        elif char.isdigit():
            has_digit = True
        # Check for space
        elif char.isspace():
            return False  # Password contains a space, so it's invalid
        
    # Check if all required character types are present
    return has_lowercase and has_uppercase and has_digit
