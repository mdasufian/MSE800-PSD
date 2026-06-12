"""Password hashing utilities.

Uses PBKDF2-HMAC-SHA256 from the Python standard library so no
third-party crypto dependency is required. Each password gets its
own random salt so identical passwords produce different hashes.
"""

import hashlib
import os


# Number of PBKDF2 iterations. Higher = slower brute force.
_ITERATIONS = 200_000


def generate_salt() -> str:
    # 16 random bytes encoded as hex; suitable as a per-user salt.
    return os.urandom(16).hex()


def hash_password(password: str, salt: str) -> str:
    # Derive a hex-encoded hash from the password + salt using PBKDF2.
    derived = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        bytes.fromhex(salt),
        _ITERATIONS,
    )
    return derived.hex()


def verify_password(password: str, salt: str, expected_hash: str) -> bool:
    # Constant-time comparison to avoid timing attacks.
    candidate = hash_password(password, salt)
    return _constant_time_equals(candidate, expected_hash)


def _constant_time_equals(a: str, b: str) -> bool:
    # Compare two strings in constant time relative to their length.
    if len(a) != len(b):
        return False
    result = 0
    for x, y in zip(a, b):
        result |= ord(x) ^ ord(y)
    return result == 0
