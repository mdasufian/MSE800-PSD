"""User domain model.

A small dataclass-like container that represents a registered user.
Kept separate from persistence so that storage format can change
without affecting business logic.
"""

from dataclasses import dataclass, asdict
from datetime import date


@dataclass
class User:
    username: str       # unique login identifier
    full_name: str      # user's full legal name
    dob: str            # date of birth in ISO format (YYYY-MM-DD)
    password_hash: str  # salted + hashed password (never plaintext)
    salt: str           # per-user random salt used with the hash

    def to_dict(self) -> dict:
        # Convert to a plain dict for JSON serialization.
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        # Rebuild a User instance from a dict loaded from JSON.
        return cls(**data)

    def age(self) -> int:
        # Compute current age from the stored DOB.
        birth = date.fromisoformat(self.dob)
        today = date.today()
        return today.year - birth.year - (
            (today.month, today.day) < (birth.month, birth.day)
        )
