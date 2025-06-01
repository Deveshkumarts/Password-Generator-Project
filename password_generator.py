import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("Select at least one character type.")

    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        special = input("Include special characters? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, upper, lower, digits, special)
        print("\nGenerated Password:", password)
    except Exception as e:
        print(f"Error: {e}")
