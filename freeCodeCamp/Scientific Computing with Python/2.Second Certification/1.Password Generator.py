# Password Generator
import re
import secrets
import string

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    # Define possible character sets for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate a random password of specified length
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        # A regular expression (regex) defines a pattern to match specific character combinations in a string.
        # It’s useful for validation, pattern matching, or character replacement, often replacing if/else logic.
        constraints = [
            (nums, r'\d'),             # Match digits
            (special_chars, fr'[{symbols}]'),  # Match special characters (escaped for regex)
            (uppercase, r'[A-Z]'),     # Match uppercase letters
            (lowercase, r'[a-z]')      # Match lowercase letters
        ]

        # Check if password meets all minimum character type requirements
        # Generator expression saves memory compared to a list comprehension by using () instead of [].
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password

if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)


