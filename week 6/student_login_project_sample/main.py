from users import (
    student_login,
    submit_assignment,
    view_grades
)


def main():

    # Call 1: a login event — single positional argument.
    student_login("Mohammad")

    # Call 2: an assignment submission — two positional arguments, forwarded
    # to the decorator's wrapper through *args.
    submit_assignment(
        "Mohammad",
        "Python Decorator Project"
    )

    # Call 3: viewing grades — note the username differs ("Alex")
    view_grades("Alex")


if __name__ == "__main__":
    main()