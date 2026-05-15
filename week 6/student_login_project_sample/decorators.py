from datetime import datetime


# Decorator factory: takes the original function `func` as input and returns
# a new function (`wrapper`) that adds logging behaviour around it.
# function's name (e.g. "student_login") when called from users.py.
def log_activity(func):

    # The wrapper replaces the original function. It accepts arbitrary
    # positional (*args) and keyword (**kwargs) arguments so that it can
    # decorate any function signature — important here because the three
    # decorated functions in users.py take different numbers of arguments.
    def wrapper(*args, **kwargs):
        # Pre-call logging: prints a banner, the function name, and a
        # timestamp so we can trace the order/timing of user actions.
        print("===================================")
        print(f"Function: {func.__name__}")
        print(f"Time: {datetime.now()}")
        print("Activity started...")

        # Execute the original (decorated) function with its original args
        # and capture the return value so it can be passed back to the caller.
        # Debugging note: forgetting to return `result` would silently swallow
        # any value the wrapped function returns — a common decorator bug.
        result = func(*args, **kwargs)

        # Post-call logging: closing banner indicating the activity finished.
        print("Activity completed.")
        print("===================================\n")

        return result

    # Return the wrapper so that `@log_activity` replaces the original
    # function with this enhanced version.
    return wrapper