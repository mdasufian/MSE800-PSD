from decorator import validate_password


# The decorator runs first and only allows this function to execute
# when the password passes validation.
@validate_password
def login(username, password):
    print(f"Login function: Welcome {username} to the Zoo Admin Panel!")
