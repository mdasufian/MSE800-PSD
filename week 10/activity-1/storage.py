"""Persistence layer.

Stores users in a local JSON file. The auth layer talks only to this
module, so the storage backend (JSON today, SQLite later) can be
swapped without touching business logic.
"""

import json
import os
from typing import Optional

from user import User


# Default data file lives next to this module.
_DATA_FILE = os.path.join(os.path.dirname(__file__), "users.json")


def _load_all() -> dict[str, dict]:
    # Read the entire user store. Returns {} if the file is missing.
    if not os.path.exists(_DATA_FILE):
        return {}
    try:
        with open(_DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        # Corrupt or unreadable file - treat as empty to avoid crashing.
        return {}


def _save_all(data: dict[str, dict]) -> None:
    # Write the user store atomically-ish (truncate + write).
    with open(_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def get_user(username: str) -> Optional[User]:
    # Look up a single user by username (case-insensitive).
    data = _load_all()
    record = data.get(username.lower())
    return User.from_dict(record) if record else None


def save_user(user: User) -> None:
    # Insert or update a user record, keyed by lowercase username.
    data = _load_all()
    data[user.username.lower()] = user.to_dict()
    _save_all(data)


def user_exists(username: str) -> bool:
    # Convenience check used during registration.
    return get_user(username) is not None
