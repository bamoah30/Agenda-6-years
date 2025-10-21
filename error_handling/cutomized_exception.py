class PasswordError(Exception):
    """Custom exception for password validation errors."""
    def __init__(self, message):
        self.message = message

def validate_password(password):
    """Validate the given password against specific criteria."""
    if len(password) < 8:
        raise PasswordError("Password must be at least 8 characters long.")
    if not any(char.isdigit() for char in password):
        raise PasswordError("Password must contain at least one digit.")
    if not any(char.isupper() for char in password):
        raise PasswordError("Password must contain at least one uppercase letter.")
    if not any(char.islower() for char in password):
        raise PasswordError("Password must contain at least one lowercase letter.")
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password):
        raise PasswordError("Password must contain at least one special character.")
    return True



# Example usagetry:
user_password = input("Enter your password for validation: ")
try:
    validate_password(user_password)
    print("Password is valid.")
except PasswordError as pe:
    print("Password validation error:", pe.message)