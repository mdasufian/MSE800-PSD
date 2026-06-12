"""Console UI entry point.

Drives a simple menu loop and delegates all real work to the auth
service. This file should stay free of business rules so the UI can
be swapped (CLI -> web -> GUI) without touching auth or storage.
"""

from getpass import getpass

import auth


def _prompt(label: str) -> str:
    # Thin wrapper around input() so we can stub it out in tests later.
    return input(label).strip()


def _prompt_password(label: str) -> str:
    # getpass hides typed characters; falls back to input on some IDEs.
    try:
        return getpass(label)
    except Exception:
        return input(label)


def _print_header(title: str) -> None:
    # Cosmetic divider used between menu screens.
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40)


def handle_register() -> None:
    """Collect registration data and call the auth service."""
    _print_header("Register New Account")
    username = _prompt("Username (3-20 chars): ")
    password = _prompt_password("Password (>=8 chars, letters + digits): ")
    full_name = _prompt("Full name: ")
    dob = _prompt("Date of birth (YYYY-MM-DD): ")

    ok, msg = auth.register(username, password, full_name, dob)
    print(f"\n{'[OK]' if ok else '[ERROR]'} {msg}")


def handle_login() -> None:
    """Prompt for credentials and show the user dashboard on success."""
    _print_header("Login")
    username = _prompt("Username: ")
    password = _prompt_password("Password: ")

    ok, msg, user = auth.login(username, password)
    print(f"\n{'[OK]' if ok else '[ERROR]'} {msg}")
    if ok and user is not None:
        _show_profile(user)


def handle_forgot_password() -> None:
    """Verify identity by DOB, then let the user set a new password."""
    _print_header("Forgot Password")
    username = _prompt("Username: ")
    dob = _prompt("Date of birth on file (YYYY-MM-DD): ")
    new_password = _prompt_password("New password: ")

    ok, msg = auth.reset_password(username, dob, new_password)
    print(f"\n{'[OK]' if ok else '[ERROR]'} {msg}")


def _show_profile(user) -> None:
    # Read-only dashboard shown after a successful login.
    _print_header("Your Profile")
    print(f"Username : {user.username}")
    print(f"Full name: {user.full_name}")
    print(f"DOB      : {user.dob}  (age {user.age()})")


def main() -> None:
    """Top-level menu loop."""
    actions = {
        "1": ("Register", handle_register),
        "2": ("Login", handle_login),
        "3": ("Forgot password", handle_forgot_password),
        "4": ("Exit", None),
    }

    while True:
        _print_header("User Account Management")
        for key, (label, _) in actions.items():
            print(f"  {key}. {label}")
        choice = _prompt("\nChoose an option: ")

        if choice == "4":
            print("Goodbye.")
            return
        action = actions.get(choice)
        if action is None:
            print("[ERROR] Invalid choice. Please pick 1-4.")
            continue
        # Each handler manages its own prompts and feedback.
        action[1]()


if __name__ == "__main__":
    main()
