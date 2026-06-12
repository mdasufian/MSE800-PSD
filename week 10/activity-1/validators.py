"""Input validation helpers.

Each validator returns (is_valid, error_message). Keeping validation
isolated from the UI and auth layers makes rules easy to evolve and
unit-test independently.
"""

import re
from datetime import date


def validate_username(username: str) -> tuple[bool, str]:
    # Username: 3-20 chars, alphanumeric or underscore only.
    if not username:
        return False, "Username cannot be empty."
    if not re.fullmatch(r"[A-Za-z0-9_]{3,20}", username):
        return False, "Username must be 3-20 chars (letters, digits, underscore)."
    return True, ""


def validate_password(password: str) -> tuple[bool, str]:
    # Password policy: >=8 chars, at least one letter and one digit.
    if len(password) < 8:
        return False, "Password must be at least 8 characters."
    if not re.search(r"[A-Za-z]", password):
        return False, "Password must contain at least one letter."
    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit."
    return True, ""


def validate_full_name(name: str) -> tuple[bool, str]:
    # Full name: non-empty, letters/spaces/hyphens/apostrophes only.
    if not name.strip():
        return False, "Full name cannot be empty."
    if not re.fullmatch(r"[A-Za-z\s\-']{2,60}", name.strip()):
        return False, "Full name contains invalid characters."
    return True, ""


def validate_dob(dob_str: str) -> tuple[bool, str]:
    # DOB must be ISO format and in the past, with a reasonable upper bound.
    try:
        dob = date.fromisoformat(dob_str)
    except ValueError:
        return False, "Date of birth must be in YYYY-MM-DD format."
    today = date.today()
    if dob >= today:
        return False, "Date of birth must be in the past."
    if (today.year - dob.year) > 120:
        return False, "Date of birth is unrealistically far in the past."
    return True, ""
