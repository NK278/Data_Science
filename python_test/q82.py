class PasswordError(Exception):
    pass

def check_password(password):
    # Check password criteria
    if len(password) < 8:
        raise PasswordError("Error: password must be at least 8 characters long.")
    elif not any(char.isupper() for char in password):
        raise PasswordError("Error: password must contain at least one uppercase letter.")
    elif not any(char.isdigit() for char in password):
        raise PasswordError("Error: password must contain at least one digit.")
    elif not any(char in ['$', '#', '@'] for char in password):
        raise PasswordError("Error: password must contain at least one of the following special characters: $ # @")
    else:
        print("Password is valid.")

# Prompt user for password
password = input("Enter a password: ")

# Check password
try:
    check_password(password)
except PasswordError as e:
    print(e)