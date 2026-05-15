# Decorator that validates the password length before calling the login function.
def validate_password(func):
    def wrapper(username, password):
        # Rule: password must be at least 8 characters
        if len(password) >= 8:
            print("Decorator: Password is valid (at least 8 characters).")
            func(username, password)  # call the original login function
            return "Success"
        else:
            print("Decorator: Password is invalid (must be at least 8 characters).")
            return "Failed"
    return wrapper
