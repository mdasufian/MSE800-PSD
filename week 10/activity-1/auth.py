"""Authentication service.

Coordinates validation, hashing, and persistence to provide the three
account features the assignment requires:
  1. register       - create a new account
  2. login          - authenticate an existing account
  3. reset_password - "forgot password" flow verified by DOB

Each function returns (success, message[, user]) so the UI layer can
print friendly feedback without knowing how auth works internally.
"""

from typing import Optional

import security
import storage
import validators
from user import User


def register(
    username: str,
    password: str,
    full_name: str,
    dob: str,
) -> tuple[bool, str]:
    """Create a new account after validating all fields."""

    # Run every validator up-front so the user sees the first problem.
    for ok, msg in (
        validators.validate_username(username),
        validators.validate_password(password),
        validators.validate_full_name(full_name),
        validators.validate_dob(dob),
    ):
        if not ok:
            return False, msg

    # Reject duplicate usernames (case-insensitive).
    if storage.user_exists(username):
        return False, "Username is already taken."

    # Generate a per-user salt used to hash the password.
    salt = security.generate_salt()
    user = User(
        username=username,
        full_name=full_name.strip(),
        dob=dob,
        password_hash=security.hash_password(password, salt),
        salt=salt,
    )
    storage.save_user(user)
    return True, "Registration successful."


def login(username: str, password: str) -> tuple[bool, str, Optional[User]]:
    """Authenticate by username and password."""

    user = storage.get_user(username)
    # Use a generic message either way to avoid leaking which usernames exist.
    if user is None:
        return False, "Invalid username or password.", None
    if not security.verify_password(password, user.salt, user.password_hash):
        return False, "Invalid username or password.", None
    return True, f"Welcome back, {user.full_name}!", user


def reset_password(
    username: str, dob: str, new_password: str
) -> tuple[bool, str]:
    """Reset password if the supplied DOB matches the account on file."""

    user = storage.get_user(username)
    if user is None:
        # Generic message so we don't reveal whether the username exists.
        return False, "Unable to reset password. Please check your details."

    # Identity check: the DOB on file must match what the user typed.
    if user.dob != dob.strip():
        return False, "Unable to reset password. Please check your details."

    # Enforce the same password policy as registration.
    ok, msg = validators.validate_password(new_password)
    if not ok:
        return False, msg

    # Rotate the salt on reset so the new hash is fully independent.
    new_salt = security.generate_salt()
    user.salt = new_salt
    user.password_hash = security.hash_password(new_password, new_salt)
    storage.save_user(user)
    return True, "Password has been reset successfully."
