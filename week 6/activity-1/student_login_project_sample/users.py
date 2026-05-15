from decorators import log_activity


# student_login: simulates a student logging into the system.
# The @log_activity decorator wraps this function so that every call is
# automatically preceded and followed by log output (function name + time).
# Debugging note: traced execution and confirmed the wrapper runs first,
# then the original print statement, then the closing log lines.
@log_activity
def student_login(username):
    print(f"{username} logged into the system.")


# submit_assignment: simulates a student submitting an assignment.
# Takes two arguments — decorator's *args/**kwargs handling means we did
# NOT need to modify the decorator to support a different signature.
# Debugging note: verified both arguments are forwarded correctly via *args.
@log_activity
def submit_assignment(username, assignment):
    print(f"{username} submitted {assignment}.")


# view_grades: simulates a student viewing their grades.
# Same decorator reuse pattern — single function definition, automatic logging
# without writing repeated print statements inside each function body.
# Debugging note: confirmed that decorating multiple functions does not cause
# any shared/mutable state issues — each call creates its own wrapper frame.
@log_activity
def view_grades(username):
    print(f"{username} is viewing grades.")